const socket = new WebSocket('ws://localhost:5000');

socket.onopen = function(event) {
    console.log('WebSocket is connected.');
};

socket.onmessage = function(event) {
    console.log('Received data:', event.data);
};

function sendData(value) {
    socket.send(JSON.stringify({ value: value }));
}
