import asyncio
import websockets
import json
import sqlite3

# Database interaction function
def interact_with_db(data):
    """
    Function to interact with a SQLite database. 
    Assumes the database and table are already created.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Insert data into the database
        cursor.execute("INSERT INTO data (value) VALUES (?)", (data['value'],))
        conn.commit()
        
        result = "Data successfully processed and stored in DLVD."
    except sqlite3.Error as e:
        result = f"Failed to process data in DLVD: {str(e)}"
    finally:
        conn.close()
    
    return result

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received data from client: {message}")
        
        # Parse the received message
        data = json.loads(message)
        
        # Interact with the DLVD
        result = interact_with_db(data)
        
        # Send the result back to the client
        await websocket.send(result)

# Start the WebSocket server
start_server = websockets.serve(handle_client, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
