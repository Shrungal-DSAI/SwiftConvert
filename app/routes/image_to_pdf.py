from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import os
import uuid
import logging

router = APIRouter()

@router.post("/image-to-pdf")
async def image_to_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(status_code=400, detail="Only JPG and PNG files are supported.")

    try:
        input_dir = "temp_inputs"
        output_dir = "temp_outputs"
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        file_id = str(uuid.uuid4())
        input_path = os.path.join(input_dir, f"{file_id}_{file.filename}")
        output_pdf_path = os.path.join(output_dir, f"{file_id}.pdf")

        with open(input_path, "wb") as f:
            f.write(await file.read())
        logging.info(f"📸 Image received: {input_path}")

        image = Image.open(input_path).convert("RGB")
        image.save(output_pdf_path, "PDF")
        logging.info(f"✅ Image converted to PDF: {output_pdf_path}")

        return FileResponse(output_pdf_path, media_type="application/pdf", filename=f"{file_id}.pdf")

    except Exception as e:
        logging.error(f"❌ Error converting image to PDF: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    finally:
        if os.path.exists(input_path):
            os.remove(input_path)
