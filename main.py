from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import os
import shutil
import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "✅ SwiftConvert API is running. Visit /docs to use it."}

@app.post("/image-to-pdf")
async def image_to_pdf(files: list[UploadFile] = File(...)):
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    image_list = []

    for file in files:
        input_path = os.path.join(temp_dir, file.filename)
        with open(input_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        img = Image.open(input_path).convert("RGB")
        image_list.append(img)

    # Save all images as one PDF
    output_filename = f"{uuid.uuid4().hex}.pdf"
    output_path = os.path.join(temp_dir, output_filename)

    if image_list:
        image_list[0].save(output_path, save_all=True, append_images=image_list[1:])

    return FileResponse(output_path, media_type='application/pdf', filename=output_filename)