var blob = new Blob([
`
    importScripts('https://cdn.jsdelivr.net/npm/sails.io.js-dist@1.2.1/sails.io.min.js');
    io.sails.url = 'http://localhost:1337';
    //let mySocket = io.connect('http://localhost:1337');
    let lectureid;

    onmessage = (e) => {
        // the passed-in data is available via e.data
        console.log(e);
        if (e.data.startRead){
            lectureid = e.data.lectureid;
            let eventName = 'lecture_'+lectureid;
            console.log(eventName);
            io.socket.on(eventName, (message) => {
                //console.log(message);
                postMessage(message);
            });
        }
    };
`
]);
/*
// Obtain a blob URL reference to our worker 'file'.
var blobURL = window.URL.createObjectURL(blob);

var worker = new Worker(blobURL);
worker.onmessage = function(e) {
  // e.data == 'msg from worker'
};
worker.postMessage(); // Start the worker.
*/

var w;
var blobURL = window.URL.createObjectURL(blob);
let numStudents = 0;
let numPoints = 0;
let sumAvgTotal = 0.0;
let avgTotal = 0.0;
let avgTotalArr = [];
let sumAvgTotalEmotion;
let studentDataObj = {};
let avgTotalArrEm = {
    anger : [], happy : [], sad : [], surprised : []
};
let lastAttentionSeq = -1;
let renderNow = false;
let lastRenderCycle = -1;
//var mySocket = io.sails.connect();

function startWorker()
{
    if(typeof(Worker)!=="undefined")            //check whether the user's browser supports it
    {
        w=new Worker(blobURL);          //creates a new web worker object and runs the code in "demo_workers.js"

        //Add an "onmessage" event listener to the web worker
        //When the web worker posts a message, the code within the event listener is executed. The data from the web worker
        //is stored in event.data.
        w.onmessage = function (event) {
            //console.log(event); 
            //document.getElementById("result").innerHTML+=event.data.a; 
            let maxPoints = 0;
            let message = event.data;
            studentDataObj = {};
            numStudents = 0;
            sumAvgTotal = 0.0;
            sumAvgTotalEmotion = {anger: 0.0, happy: 0.0, sad: 0.0, surprised: 0.0};
            _.forEach(message, (k, v)=>{
                if (!_.isEmpty(v) && _.isNumber(k.avgAttentionCurrent) && k.attentionSeq != lastAttentionSeq){
                    let studentid = v;
                    let studentData = k;
                    numStudents += 1;
                    sumAvgTotal += k.avgAttentionCurrent;
                    studentDataObj[studentid] = k.avgAttentionCurrent;
                    if (studentData.totalAttentionSum > maxPoints){
                        maxPoints = studentData.totalAttentionSum;
                    }
                    sumAvgTotalEmotion.anger += k.emCurrent.anger;
                    sumAvgTotalEmotion.happy += k.emCurrent.happy;
                    sumAvgTotalEmotion.sad += k.emCurrent.sad;
                    sumAvgTotalEmotion.surprised += k.emCurrent.surprised;
                    lastAttentionSeq = k.attentionSeq;
                    renderNow = true;
                } else {
                    renderNow = false;
                }
            });
            if (numStudents > 0){
                avgTotal = sumAvgTotal/numStudents;
                avgTotalArr.push(avgTotal*100);
                avgTotalArrEm.anger.push((sumAvgTotalEmotion.anger/numStudents)*100);
                avgTotalArrEm.happy.push((sumAvgTotalEmotion.happy/numStudents)*100);
                avgTotalArrEm.sad.push((sumAvgTotalEmotion.sad/numStudents)*100);
                avgTotalArrEm.surprised.push((sumAvgTotalEmotion.surprised/numStudents)*100);
                //set to list
                let displayStudentStr = ``;
                _.each(studentDataObj, (k,v)=>{
                    if (_.isNumber(k)){
                        displayStudentStr += `<p>Student id: ${k} AttentionLevel: ${v} StudentGraph: <a>Click Here.</a> </p>`;
                    }
                });
                document.getElementById("connectedStudents").innerHTML = displayStudentStr;
            }
        };
        sendLectureidAndStartRead();
    }
    else
    {
        document.getElementById("result").innerHTML="Sorry, your browser does not support Web Workers...";
    }
}

function stopWorker()
{ 
    w.terminate();         //terminate a web worker, and free browser/computer resources
}

function sendLectureidAndStartRead(){
    w.postMessage({'lectureid':lectureidForJS, 'startRead':true});
}

//startWorker();
window.onload = function () {

    var dps = []; // dataPoints
    var dpsEmAnger = []; // dataPoints
    var dpsEmHappy = []; // dataPoints
    var dpsEmSad = []; // dataPoints
    var dpsEmSurprised = []; // dataPoints
    var chart = new CanvasJS.Chart("chartContainer", {
        title :{
            text: "Attention Data"
        },
        axisY: {
            includeZero: false
        },      
        data: [{
            type: "line",
            name: "Attention Value",
            showInLegend: true,
            dataPoints: dps
        }]
    });

    var emotionChart = new CanvasJS.Chart("emotionChartContainer", {
        title :{
            text: "Emotion Data"
        },
        axisY: {
            includeZero: false
        },      
        data: [{
            type: "line",
            name: "Anger Value",
            showInLegend: true,
            dataPoints: dpsEmAnger
        },
        {
            type: "line",
            name: "happy Value",
            showInLegend: true,
            dataPoints: dpsEmHappy
        },
        {
            type: "line",
            name: "Sad Value",
            showInLegend: true,
            dataPoints: dpsEmSad
        },
        {
            type: "line",
            name: "Surprised Value",
            showInLegend: true,
            dataPoints: dpsEmSurprised
        }]
    });

    var xVal = 0;
    var yVal = 100; 
    var updateInterval = 1000;
    var dataLength = 20; // number of dataPoints visible at any point

    var updateChart = function () {
        //render only if last data recvd seq matches with the last render cycle
        console.log(lastRenderCycle, lastAttentionSeq);
        if (lastRenderCycle != lastAttentionSeq){
            if (avgTotalArr.length > 0){
                dps.push({
                    x: xVal, 
                    y: avgTotalArr[avgTotalArr.length-1]
                });
                dpsEmAnger.push({
                    x: xVal, 
                    y: avgTotalArrEm.anger[avgTotalArrEm.anger.length-1]
                });
                dpsEmHappy.push({
                    x: xVal, 
                    y: avgTotalArrEm.happy[avgTotalArrEm.happy.length-1]
                });
                dpsEmSad.push({
                    x: xVal, 
                    y: avgTotalArrEm.sad[avgTotalArrEm.sad.length-1]
                });
                dpsEmSurprised.push({
                    x: xVal, 
                    y: avgTotalArrEm.surprised[avgTotalArrEm.surprised.length-1]
                });
                xVal += 1;
            }

            if (dps.length > 0 && renderNow){
                chart.render();
            }

            if (dpsEmAnger.length > 0 && renderNow){
                emotionChart.render();
            }

            lastRenderCycle = lastAttentionSeq;
        } else {
            // do not render
        }
    };

    //updateChart(dataLength);
    setInterval(function(){updateChart()}, updateInterval);

}