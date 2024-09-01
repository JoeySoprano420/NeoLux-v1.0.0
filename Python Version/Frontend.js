const socket = new WebSocket('ws://localhost:5000');

// Event handler for when the WebSocket connection is established
socket.onopen = function(event) {
    console.log('WebSocket is connected.');
};

// Event handler for when a message is received from the WebSocket server
socket.onmessage = function(event) {
    console.log('Received data:', event.data);
};

// Function to send data to the WebSocket server
function sendData(key, value) {
    const data = { key: key, value: value };
    socket.send(JSON.stringify(data));
}

// Example usage
sendData('exampleKey', 'exampleValue');
