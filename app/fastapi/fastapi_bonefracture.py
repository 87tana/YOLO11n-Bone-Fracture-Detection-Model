from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse, StreamingResponse
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Load YOLO model globally (to avoid loading it on every request)
model = YOLO("yolov11n_best.pt")

# Root route to handle requests to "/"
@app.get("/")
async def root():
    return {"message": "Welcome to the YOLO Object Detection API"}

# Object detection route
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...), conf_threshold: float = Form(...)):
    try:
        # Read the uploaded image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        image_np = np.array(image)

        # Apply YOLO to the image
        results = model.predict(image_np, conf=conf_threshold, augment=True)

        # Annotate the image with bounding boxes
        annotated_image = results[0].plot()

        # Convert annotated image back to bytes
        annotated_pil = Image.fromarray(annotated_image)
        buffer = io.BytesIO()
        annotated_pil.save(buffer, format="PNG")
        buffer.seek(0)

        return StreamingResponse(buffer, media_type="image/png")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


