# 🛠️ SwiftConvert – Project Plan

A full-stack file conversion platform focused on **efficiency**, **durability**, and **scalability** using FastAPI.

---

## ✅ Project Goals

Create a file conversion app that supports:

- 🔄 PDF ↔ Word (with and without OCR)
- 🖼️ Image → PDF
- 🧾 Batch conversion support
- 🔐 User Authentication (future)
- 🐳 Docker + CI/CD
- 🧩 Modular architecture (microservices)

---

## ✅ Phase 1: Core Setup

| Task                            | Status   | Notes                          |
|---------------------------------|----------|--------------------------------|
| ✅ Create GitHub Repo           | ✅ Done  | Public repo `swiftconvert`    |
| ✅ Add README.md + .gitignore   | ✅ Done  | Python-based project           |
| ✅ Set up virtual environment   | ✅ Done  | `venv` activated               |
| ✅ FastAPI initial setup        | ✅ Done  | `/docs` route active           |
| ✅ Implement PDF → Word (no OCR)| ✅ Done  | Uses `PyMuPDF (fitz)`         |
| ✅ Implement PDF → Word (OCR)   | ✅ Done  | Uses `Tesseract + python-docx` |
| ✅ Install requirements via pip | ✅ Done  | All dependencies working       |
| ✅ Launch Uvicorn server        | ✅ Done  | Runs at `http://127.0.0.1:8000`|
| ✅ Dockerize the project        | ✅ Done  | Working container built        |

---

## 🧠 Phase 2: Architecture Best Practices

| Task                         | Status       | Notes                                   |
|------------------------------|--------------|-----------------------------------------|
| 🔲 Refactor into microservices | ⏳ In Progress | Use modular routes (`/ocr`, `/img2pdf`) |
| ✅ Add Docker + Docker Compose | ✅ Done      | Dockerfile complete, Compose pending    |
| 🔲 Setup .env for config       | 🔲 Not Started | Use `python-dotenv` or Pydantic         |
| 🔲 Optimize file handling      | 🔲 Not Started | For large/batch files                   |
| 🔲 Support batch uploads       | 🔲 Not Started | Zip or multiple file processing         |

---

## 🚨 Phase 3: Error Handling & Security

| Task                        | Status        | Notes                                 |
|-----------------------------|---------------|----------------------------------------|
| 🔲 Add custom error handling | 🔲 Not Started | JSON responses with FastAPI exception |
| 🔲 Validate file types/sizes | 🔲 Not Started | Limit abuse and large files           |
| 🔲 Sanitize file names       | 🔲 Not Started | Avoid filesystem exploits              |
| 🔲 Scan for malicious files  | 🔲 Not Started | Optional: ClamAV or similar            |

---

## ⚙️ Phase 4: Background Jobs (Celery + Redis)

| Task                         | Status        | Notes                             |
|------------------------------|---------------|------------------------------------|
| 🔲 Set up Redis via Docker   | 🔲 Not Started | Acts as Celery broker              |
| 🔲 Install and configure Celery | 🔲 Not Started | Async background job processing   |
| 🔲 Offload heavy conversions | 🔲 Not Started | Prevent FastAPI timeouts           |
| 🔲 Optional job status API   | 🔲 Not Started | Monitor task progress              |

---

## 🧪 Phase 5: Testing & CI/CD

| Task                       | Status        | Notes                             |
|----------------------------|---------------|------------------------------------|
| 🔲 Unit tests with pytest  | 🔲 Not Started | API and I/O validation             |
| 🔲 Edge case testing       | 🔲 Not Started | Handle large and corrupt files     |
| 🔲 GitHub Actions CI       | 🔲 Not Started | Automated build + test on push     |
| 🔲 Create test suite folder| 🔲 Not Started | Organize under `/tests/`           |

---

## 📊 Phase 6: Monitoring & Logs

| Task                      | Status        | Notes                             |
|---------------------------|---------------|------------------------------------|
| 🔲 Add logging system     | 🔲 Not Started | Console + file logs                |
| 🔲 Integrate Sentry       | 🔲 Not Started | Exception reporting                |
| 🔲 Prometheus + Grafana   | 🔲 Not Started | Performance tracking (optional)    |

---

## 🎨 Phase 7: Frontend (Optional)

| Task                        | Status        | Notes                            |
|-----------------------------|---------------|-----------------------------------|
| 🔲 Build frontend interface | 🔲 Not Started | HTML or React/Vite                |
| 🔲 Upload progress bar      | 🔲 Not Started | Better UX                         |
| 🔲 Download result link     | 🔲 Not Started | User can download converted files |

---

## 🔐 Phase 8: User Authentication (Optional)

| Task                       | Status        | Notes                              |
|----------------------------|---------------|-------------------------------------|
| 🔲 Add login/signup system | 🔲 Not Started | JWT or OAuth2                       |
| 🔲 Track user file history | 🔲 Not Started | Conversion history per account      |
| 🔲 Apply user quotas       | 🔲 Not Started | Prevent misuse by limiting traffic  |

---

## 📁 Suggested Folder Structure

```
swiftconvert/
├── app/
│   ├── main.py
│   └── routes/
│       ├── pdf_to_word_no_ocr.py
│       ├── pdf_to_word_ocr.py
│       └── image_to_pdf.py
├── Dockerfile
├── requirements.txt
├── README.md
├── projectplan.md
└── .env (optional)
```

---

## ✅ Summary

- **✅ Completed:** 10 core tasks  
- **⏳ In Progress:** 1 task  
- **🔲 Remaining:** 25+ tasks to go  
- 🧩 This roadmap will evolve as we progress to v2.0 and beyond.

---

🎯 **Focus going forward:**  
Stability, batch processing, CI/CD, file validation, and microservice refactor.

🧠 Built to scale.  
💻 Built for developers.  
🚀 Built for production.
