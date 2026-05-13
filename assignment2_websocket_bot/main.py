from fastapi import FastAPI, WebSocket, WebSocketDisconnect 
import uvicorn

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("client connected")
    
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message: {data}")
        
            response = f"Echo: {data}"
            await websocket.send_text(response)
            print(f"Sent response: {response}")
    
    except WebSocketDisconnect:
        print("client disconnected")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)