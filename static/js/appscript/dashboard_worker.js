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
                console.log(message);
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
            console.log(event); 
            document.getElementById("result").innerHTML+=event.data.a; 
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