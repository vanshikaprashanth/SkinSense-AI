from io import BytesIO
import numpy as np
from PIL import Image, ImageOps

def make_preview(uploaded_file):
    image = ImageOps.exif_transpose(Image.open(BytesIO(uploaded_file.getvalue()))).convert("RGB")
    preview = image.copy()
    preview.thumbnail((900, 900))
    return preview, image

def analyze_image(image):
    arr = np.asarray(image, dtype=np.float32)
    return {"width": image.width, "height": image.height, "brightness": float(arr.mean())}
