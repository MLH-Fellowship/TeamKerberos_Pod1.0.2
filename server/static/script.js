//Todo- Implement Client side camera capture

// navigator.getUserMedia = ( navigator.getUserMedia ||
//   navigator.webkitGetUserMedia ||
//   navigator.mozGetUserMedia ||
//   navigator.msGetUserMedia);

// function startVideo() {
// console.log("access");
// navigator.getUserMedia(
//   {
//     video: {}
//   },
//   stream => video.srcObject = stream,
//   err => console.error(err)
//   )}

var word = "";

document.addEventListener("DOMContentLoaded", function(event) {
    const image_elem = document.getElementById("streamer-image");
    const text_elem = document.getElementById("streamer-text");

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/web', {
      reconnection: false
    });

    socket.on('connect', () => {
      console.log('Connected');
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

    // Update image and text data based on incoming data messages
    socket.on('server2web', (msg) => {
      image_elem.src = msg.image;
      if (msg.text !== "nothing"){
        word = word + msg.text
        text_elem.innerHTML = word;
      }
    });
  });