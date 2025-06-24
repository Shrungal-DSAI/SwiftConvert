from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
import uuid
import logging
import traceback
from app.utils.ocr_with_layoutparser import convert_pdf_to_docx_with_ocr

router = APIRouter()

@router.post("/pdf-to-word-ocr")
async def pdf_to_word_ocr(file: UploadFile = File(...)):
    input_pdf_path = None
    output_docx_path = None

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file.file.seek(0, os.SEEK_END)
    file_size = file.file.tell()
    file.file.seek(0)
    if file_size > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Max 10MB allowed.")

    try:
        input_dir = "temp_inputs"
        output_dir = "temp_outputs"
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        file_id = str(uuid.uuid4())
        input_pdf_path = os.path.join(input_dir, f"{file_id}.pdf")
        output_docx_path = os.path.join(output_dir, f"{file_id}.docx")

        with open(input_pdf_path, "wb") as f:
            f.write(await file.read())
        logging.info(f"📄 Starting OCR conversion for: {input_pdf_path}")

        convert_pdf_to_docx_with_ocr(input_pdf_path, output_docx_path)
        logging.info(f"✅ OCR to DOCX complete: {output_docx_path}")

        return FileResponse(
            output_docx_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=f"{file_id}.docx"
        )

    except Exception as e:
        logging.error("❌ OCR conversion failed:")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to convert PDF using OCR.")

    finally:
        # Always clean up input PDF
        if input_pdf_path and os.path.exists(input_pdf_path):
            os.remove(input_pdf_path)
        # Optional: remove output DOCX after download delay via background task or cron
