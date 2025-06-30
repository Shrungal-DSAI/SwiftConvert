from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
from docx import Document
import os
import uuid

# ✅ Set path to tesseract.exe manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = FastAPI()

@app.post("/pdf-to-word-ocr")
async def pdf_to_word_ocr(file: UploadFile = File(...)):
    # Save uploaded PDF temporarily
    temp_pdf_path = f"temp_{uuid.uuid4()}.pdf"
    with open(temp_pdf_path, "wb") as f:
        f.write(await file.read())

    # Load PDF with PyMuPDF
    doc = fitz.open(temp_pdf_path)
    ocr_texts = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=300)  # Higher DPI = better OCR
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        # Perform OCR on image
        text = pytesseract.image_to_string(image, lang="eng")
        ocr_texts.append(f"--- Page {page_num + 1} ---\n{text.strip()}\n")

    doc.close()  # ✅ Close PDF before deleting the file

    # Create Word Document
    docx_filename = f"output_{uuid.uuid4()}.docx"
    document = Document()
    for page_text in ocr_texts:
        document.add_paragraph(page_text)
        document.add_page_break()
    document.save(docx_filename)

    # Clean up temp PDF
    os.remove(temp_pdf_path)

    # Return the .docx file as download
    return FileResponse(docx_filename,
                        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        filename="converted.docx")


templates = Jinja2Templates(directory="templates")

@app.get("/upload", response_class=HTMLResponse)
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})