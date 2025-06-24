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

