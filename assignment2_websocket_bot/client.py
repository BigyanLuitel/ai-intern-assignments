import asyncio
import websockets

async def simulate_audio_stream():
    url = "ws://localhost:8000/ws"

    async with websockets.connect(url) as websocket:
        print("Connected to WebSocket server")
        
        audio_chunks = [
            "Audio chunk 1: Hello, what is my account balance?",
            "Audio chunk 2: Transfer 500 rupees to savings account.",
            "Audio chunk 3: Show my last 5 transactions."
        ]
        
        for chunk in audio_chunks:
            await websocket.send(chunk)
            print(f"Sent: {chunk}")
            
            response = await websocket.recv()
            print(f"Received: {response}")
            
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(simulate_audio_stream())