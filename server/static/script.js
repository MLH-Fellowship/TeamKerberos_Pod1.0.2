// get video dom element
const video = document.querySelector('video');
const text_elem = document.getElementById("streamer-text");


// request access to webcam
navigator.mediaDevices.getUserMedia({video: {width: 426, height: 240}}).then((stream) => video.srcObject = stream);

// returns a frame encoded in base64
const getFrame = () => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    return canvas.toDataURL();
};

var socket = io.connect('http://' + document.domain + ':' + location.port + '/web', {
    reconnection: false
});

socket.on('connect', () => {
    console.log('Connected');
    sendstream();
});

socket.on('disconnect', () => {
    console.log('Disconnected');
});

socket.on('connect_error', (error) => {
    console.log('Connect error! ' + error);
});

socket.on('connect_timeout', (error) => {
    console.log('Connect timeout! ' + error);
});

socket.on('error', (error) => {
    console.log('Error! ' + error);
});

function sendstream() {
    setInterval(() => {
        socket.emit('stream',getFrame());
    }, 1000 / 2);
}
word = "";
socket.on('server2web', (msg) => {
    if (msg.text !== "nothing"){
        word = word + msg.text;
        text_elem.innerHTML = word;
    }
});