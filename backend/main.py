import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from pdf2docx import Converter

app = FastAPI()

# Folders
UPLOAD_DIR = "uploads"
CONVERTED_DIR = "converted"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CONVERTED_DIR, exist_ok=True)

from pdf2docx import Converter

@app.post("/convert/pdf-to-word/")
async def convert_pdf_to_word(file: UploadFile = File(...)):
    file_ext = file.filename.split(".")[-1].lower()
    if file_ext != "pdf":
        return JSONResponse(status_code=400, content={"error": "Please upload a PDF file"})

    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_filename = file.filename.rsplit(".", 1)[0] + ".docx"
    output_path = os.path.join(CONVERTED_DIR, output_filename)

    # Save the uploaded PDF file
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Convert PDF to Word
    try:
        cv = Converter(input_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Conversion failed: {str(e)}"})

    return FileResponse(path=output_path, filename=output_filename, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")