import asyncio
import websockets
import json
import os

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

# Start the WebSocket server
async def start_websocket_server():
    start_server = websockets.serve(handle_client, "localhost", 5000)
    await start_server

if __name__ == '__main__':
    # Run the WebSocket server
    asyncio.get_event_loop().run_until_complete(start_websocket_server())
    asyncio.get_event_loop().run_forever()
