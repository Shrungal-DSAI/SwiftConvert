from app.routes import image_to_pdf
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import logging
from fastapi import FastAPI

# ✅ Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# ✅ Import route modules
from app.routes import pdf_to_word_ocr
from app.routes import pdf_to_word_no_ocr
from app.routes import maintenance

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Include routers
app.include_router(pdf_to_word_ocr.router)
app.include_router(pdf_to_word_no_ocr.router)
app.include_router(maintenance.router)
app.include_router(image_to_pdf.router)
# ✅ Landing route
@app.get("/")
def read_root():
    return {
        "message": "👋 Welcome to SwiftConvert!",
        "routes": [
            "/pdf-to-word-no-ocr (POST)",
            "/pdf-to-word-ocr (POST)",
            "/image-to-pdf (POST)",
            "/cleanup-temp (POST)",
            "/docs (Interactive Swagger UI)"
        ],
        "note": "Upload files using the above endpoints or test them from Swagger UI."
    }
# ✅ Serve static HTML
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/upload", response_class=HTMLResponse)
def upload_page():
    return open("app/static/index.html").read()

