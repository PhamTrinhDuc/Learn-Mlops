import base64
from loguru import logger
from io import BytesIO

import numpy as np
import uvicorn
from fastapi import FastAPI, WebSocket
from PIL import Image

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive()
            if data["type"] == "websocket.disconnect":
                break  # Thoát khỏi vòng lặp khi kết nối bị ngắt
            img = Image.open(BytesIO(data["bytes"]))
            np_img = np.array(img)
            # Send the image back to the browser
            await websocket.send({"type": "websocket.send", "bytes": data["bytes"]})
    except Exception as e:
        logger.error(f"Error in WebSocket connection: {e}")
    finally:
        logger.info("WebSocket connection closed")