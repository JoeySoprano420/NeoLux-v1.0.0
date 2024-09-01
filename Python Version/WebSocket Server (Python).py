import asyncio
import websockets
import json
import requests

# Simulated DLVD interaction via REST API
DLVD_API_URL = 'http://localhost:5001/api/data'

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received data from client: {message}")
        
        # Parse the received message
        data = json.loads(message)
        
        # Send data to DLVD and get the result via REST API
        response = requests.post(DLVD_API_URL, json=data)
        
        if response.status_code == 201:
            result = "Data successfully processed and stored in DLVD."
        else:
            result = "Failed to process data in DLVD."
        
        # Send the result back to the client
        await websocket.send(result)

# Start the WebSocket server
start_server = websockets.serve(handle_client, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
