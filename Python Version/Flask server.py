from flask import Flask, request, jsonify
import sqlite3
import asyncio
import websockets
import json
import os
from threading import Thread

# Define the path to the file-based storage for the HybridDatabase
DATA_FILE_PATH = 'data_store.json'

class HybridDatabase:
    def __init__(self):
        # Initialize the in-memory store and load from file
        self.memory_store = {}
        self.load_data()

    def load_data(self):
        """Load data from file if it exists."""
        if os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH, 'r') as file:
                self.memory_store = json.load(file)
        else:
            self.memory_store = {}

    def save_data(self):
        """Save data to file."""
        with open(DATA_FILE_PATH, 'w') as file:
            json.dump(self.memory_store, file)

    def insert_data(self, key, value):
        """Insert data into the in-memory store and save to file."""
        self.memory_store[key] = value
        self.save_data()
        return "Data successfully processed and stored."

    def query_data(self, key):
        """Query data from the in-memory store."""
        return self.memory_store.get(key, "No data found.")

# Initialize the HybridDatabase instance
db = HybridDatabase()

# Flask application setup
app = Flask(__name__)

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        if 'key' in data and 'value' in data:
            result = db.insert_data(data['key'], data['value'])
            return jsonify({'status': 'success', 'message': result}), 201
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400
    else:
        # Return all data stored in memory for simplicity
        return jsonify(db.memory_store), 200

# WebSocket server setup
async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received data from client: {message}")
        
        # Parse the received message
        data = json.loads(message)
        
        # Ensure data contains the key and value
        if 'key' in data and 'value' in data:
            result = db.insert_data(data['key'], data['value'])
        elif 'key' in data:
            result = db.query_data(data['key'])
        else:
            result = "Invalid data format."
        
        # Send the result back to the client
        await websocket.send(result)

# WebSocket server start function
async def start_websocket_server():
    start_server = websockets.serve(handle_client, "localhost", 5000)
    await start_server

# Flask and WebSocket server runner
def run_flask_app():
    app.run(port=5001, debug=True, use_reloader=False)

if __name__ == '__main__':
    # Start the WebSocket server in a separate thread
    websocket_thread = Thread(target=lambda: asyncio.run(start_websocket_server()))
    websocket_thread.start()
    
    # Start the Flask app
    run_flask_app()
