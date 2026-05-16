# Assignment 2: Asynchronous WebSocket Echo Bot

## Overview

A FastAPI server that opens a bi-directional WebSocket connection, mimicking a telephony integration like Twilio. The server receives simulated audio stream chunks and echoes responses back in real time.

## How It Works

1. **Server** — FastAPI WebSocket server listens for incoming connections on `ws://localhost:8000/ws`
2. **Client** — Simulates Twilio by sending audio chunks one at a time with a 1 second delay between each
3. **Echo** — Server receives each chunk, processes it, and sends a response back
4. **Disconnect** — Server detects client disconnect gracefully via `WebSocketDisconnect`

## Project Structure

assignment2_websocket_bot/
├── main.py # FastAPI WebSocket server
├── client.py # Simulated Twilio audio stream client
├── requirements.txt # Project dependencies
└── README.md # Project documentation

## Installation

### 1. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Start the server (Terminal 1)

```bash
python main.py
```

### 2. Run the client (Terminal 2)

```bash
python client.py
```

## Sample Output

**Server:**
Connected to WebSocket server
Sent: Audio chunk 1: Hello, what is my account balance?
Received: Echo: Audio chunk 1: Hello, what is my account balance?
Sent: Audio chunk 2: Transfer 500 rupees to savings account.
Received: Echo: Audio chunk 2: Transfer 500 rupees to savings account.

## Core Concepts

- **WebSocket** — bi-directional, persistent connection unlike HTTP
- **async/await** — handles multiple connections simultaneously without blocking
- **while True loop** — keeps connection open to receive continuous stream
- **WebSocketDisconnect** — gracefully handles client disconnection

## Connection to Real Telephony

In a real Twilio integration:

- Twilio captures user voice as audio chunks
- Streams them to this server via WebSocket
- Server processes audio (STT → LLM → TTS) and responds
- This bot simulates that stream with text messages
