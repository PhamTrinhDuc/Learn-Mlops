import os
import cv2
import easyocr
import numpy as np
from PIL import Image, ImageDraw, ImageFont

reader = easyocr.Reader(
    ["vi", "en"],
    gpu=False,
    detect_network="craft",
    model_storage_directory="./my_model",
    download_enabled=False,
)

filepath = "examples/receipt.jpg"
img = cv2.imread(filepath)
detection = reader.readtext(filepath)

# if OCR prob is over 0.5, overlay bounding box and text
fontpath = "./fonts/BeVietnam-Light.ttf"
font = ImageFont.truetype(fontpath, 15)

for bbox, text, prob in detection:
    if prob >= 0.5:
        # display
        print(f"Detected text: {text} (Probability: {prob:.2f})")
        # get top-left and bottom-right bbox vertices
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        # Create a draw on the original image using the predicted bboxes
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((top_left[0], top_left[1] - 20), text, font=font, fill=(0, 255, 0, 0))
        draw.rectangle([top_left, bottom_right], outline="green")
        img = np.array(img_pil)

cv2.imwrite(
    os.path.join(
        os.path.dirname(filepath), f"{os.path.basename(filepath)}_overlay.jpg"
    ),
    img,
)