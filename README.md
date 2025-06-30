# 🛠️ SwiftConvert

A full-stack document conversion tool powered by **FastAPI**, supporting robust **PDF ↔ Word (with and without OCR)** and **Image → PDF** conversions. Built with a modular architecture and Docker support for scalable deployment.

---

## 🚀 Features

- 🔄 Convert **PDF to Word** (with & without OCR)
- 🖼️ Convert **Image to PDF**
- 🤖 OCR support with **Tesseract** + **LayoutParser**
- 📦 Packaged with **Docker** for cross-platform deployment
- 🧪 FastAPI with interactive Swagger UI
- ⚡ Lightweight, fast, and scalable

---

## 📁 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Welcome route |
| `/pdf-to-word-no-ocr` | POST | Converts PDF to Word without OCR |
| `/pdf-to-word-ocr` | POST | Converts PDF to Word using OCR |
| `/image-to-pdf` | POST | Converts image (JPG, PNG) to PDF |

> ✅ All routes accept `multipart/form-data` with a `file` field.

---

## 🐳 Docker Setup

### 🔧 1. Build the Docker image
```bash
docker build -t swiftconvert .

### ▶️ 2. Run the container
docker run -it -p 8000:8000 swiftconvert

### 🌐 3. Open in browser
Visit: http://localhost:8000/docs

### 📌 Sample curl Usage
curl -X 'POST' \
  'http://localhost:8000/pdf-to-word-ocr' \
  -H 'accept: application/vnd.openxmlformats-officedocument.wordprocessingml.document' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample.pdf' \
  --output output.docx

### 📁 Project Structure
swiftconvert/
├── app/
│   ├── main.py
│   └── routes/
│       ├── pdf_to_word_no_ocr.py
│       ├── pdf_to_word_ocr.py
│       └── image_to_pdf.py
├── requirements.txt
├── Dockerfile
├── README.md

### ✅ Dependencies
Key libraries used:

fastapi, uvicorn

pymupdf, python-docx, pdf2image

layoutparser, pytesseract, opencv-python

torch, torchvision, torchaudio (CPU-only)

pillow, python-multipart

Install manually (optional):
pip install -r requirements.txt

### 📌 Roadmap (v1.0 Completed)
Feature	Status
PDF → Word (no OCR)	✅ Done
PDF → Word (with OCR)	✅ Done
Image → PDF	✅ Done
Docker Support	✅ Done
GitHub Public Repo	✅ Done

💡 Future plans: CI/CD, Celery + Redis, authentication, microservices

📜 License
MIT

👨‍💻 Author
Shrungal Kulkarni
Made with ❤️ for reliable document conversion
---

Let me know if you'd like badges (like Docker Hub, Python version, License, etc.) or a shorter version for a private/internal repo.
