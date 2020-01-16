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
let studentDataObj = {};
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
            _.forEach(message, (k, v)=>{
                if (!_.isEmpty(v) && _.isNumber(k.avgAttentionCurrent)){
                    let studentid = v;
                    let studentData = k;
                    numStudents += 1;
                    sumAvgTotal += k.avgAttentionCurrent;
                    studentDataObj[studentid] = k.avgAttentionCurrent;
                    if (studentData.totalAttentionSum > maxPoints){
                        maxPoints = studentData.totalAttentionSum;
                    }
                }
            });
            if (numStudents > 0){
                avgTotal = sumAvgTotal/numStudents;
                avgTotalArr.push(avgTotal*100);
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
    var chart = new CanvasJS.Chart("chartContainer", {
        title :{
            text: "Dynamic Data"
        },
        axisY: {
            includeZero: false
        },      
        data: [{
            type: "line",
            dataPoints: dps
        }]
    });

    var xVal = 0;
    var yVal = 100; 
    var updateInterval = 1000;
    var dataLength = 20; // number of dataPoints visible at any point

    var updateChart = function () {

        /*
        count = count || 1;

        for (var j = 0; j < count; j++) {
            yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
            dps.push({
                x: xVal,
                y: yVal
            });
            xVal++;
        }
        */
        if (avgTotalArr.length > 0){
            dps.push({
                x: xVal, 
                y: avgTotalArr[avgTotalArr.length-1]
            });
            xVal += 1;
        }
        /*
        let xval = 0;
        _.forEach(avgTotalArr, ata =>{
            xval+=1;
            dps.push({
                x: xval, y: ata
            });
        });
        */

        if (dps.length > 0)
            chart.render();
    };

    //updateChart(dataLength);
    setInterval(function(){updateChart()}, updateInterval);

}