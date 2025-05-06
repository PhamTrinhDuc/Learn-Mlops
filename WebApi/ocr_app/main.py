from io import BytesIO

import easyocr
import imagehash
import numpy as np
from fastapi import FastAPI, File, UploadFile
from loguru import logger
from PIL import Image

# Save all files and result to cached
# by a dictionary with key is image hash
cache = {}
app = FastAPI(root_path="/")
 

reader = easyocr.Reader(
  lang_list=['en', 'vi'],
  gpu=False, detect_network="craft",
  model_storage_directory="./my_model",
  download_enabled=False
)  

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)): 
  try:
    request_object_content = await file.read()
    # Read image from route
    image_stream = BytesIO(request_object_content)
    image_stream.seek(0)

    pil_image = Image.open(image_stream)
  except Exception as e:
    logger.error(f"Error reading image: {e}")
    return {"error": "Invalid image format"}

  # Get the detection from EasyOCR
  detection = reader.readtext(np.array(pil_image))

  # Create final result
  result = {"bboxes": [], "texts": [], "probs": []}
  for bbox, text, prob in detection:
      # Convert a list of NumPy int elements to premitive numbers
      bbox = np.array(bbox).tolist()
      result["bboxes"].append(bbox)
      result["texts"].append(text)
      result["probs"].append(prob)

  return result 

@app.post("/ocr/cache")
async def ocr_cache(file: UploadFile = File(...)):
  try:
    request_object_content = await file.read()
    # Read image from route
    image_stream = BytesIO(request_object_content)
    image_stream.seek(0)

    pil_image = Image.open(image_stream)
    pil_hash = imagehash.average_hash(pil_image)
  except Exception as e:
      logger.error(f"Error reading image: {e}")
      return {"error": "Invalid image format"}
  if pil_hash in cache:
    logger.info("Getting result from cache!")
    return cache[pil_hash]
  else:
    logger.info("Getting result from EasyOCR!")
    # Get the detection from EasyOCR
    detection = reader.readtext(np.array(pil_image))

    # Create final result
    result = {"bboxes": [], "texts": [], "probs": []}
    for bbox, text, prob in detection:
        # Convert a list of NumPy int elements to premitive numbers
        bbox = np.array(bbox).tolist()
        result["bboxes"].append(bbox)
        result["texts"].append(text)
        result["probs"].append(prob)

    # Save to cache
    cache[pil_hash] = result
    return result

# command to run the server
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload