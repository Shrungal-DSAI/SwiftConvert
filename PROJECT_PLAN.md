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

| Task | Status | Notes |
|------|--------|-------|
| ✅ Create GitHub Repo swiftconvert | ✅ Done | Public repo created |
| ✅ Add README.md + .gitignore | ✅ Done | Python-based project |
| ✅ Set up virtual environment | ✅ Done | env activated |
| ✅ FastAPI initial setup | ✅ Done | /docs route active |
| ✅ Implement PDF → Word (no OCR) | ✅ Done | Uses PyMuPDF (itz) |
| ✅ Implement PDF → Word (OCR) | ✅ Done | Uses Tesseract + python-docx |
| ✅ Install requirements via pip | ✅ Done | All modules working |
| ✅ Launch Uvicorn server | ✅ Done | http://127.0.0.1:8000 |

---

## 🧠 Phase 2: Architecture Best Practices

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Refactor into microservices | ⏳ In Progress | Use /ocr, /img2pdf, etc. |
| 🔲 Add Docker + Docker Compose | ⏳ Not Started | Use Dockerfile, docker-compose.yml |
| 🔲 Setup .env for config | ⏳ Not Started | Use python-dotenv or Pydantic |
| 🔲 Optimize memory/file handling | ⏳ Not Started | For large files |
| 🔲 Support batch uploads | ⏳ Not Started | Multiple files or zip |

---

## 🚨 Phase 3: Error Handling & Security

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Add custom error handling | ⏳ Not Started | JSON responses |
| 🔲 Validate file types/sizes | ⏳ Not Started | Prevent abuse |
| 🔲 Sanitize file names | ⏳ Not Started | Secure uploads |
| 🔲 Scan for malicious files | ⏳ Not Started | ClamAV (optional) |

---

## ⚙️ Phase 4: Background Jobs (Celery + Redis)

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Set up Redis via Docker | ⏳ Not Started | Job broker |
| 🔲 Install and configure Celery | ⏳ Not Started | Async background tasks |
| 🔲 Offload heavy conversions | ⏳ Not Started | Prevents FastAPI timeout |
| 🔲 Optional job status API | ⏳ Not Started | Monitor progress |

---

## 🧪 Phase 5: Testing & CI/CD

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Unit tests with pytest | ⏳ Not Started | Basic API & file checks |
| 🔲 Edge case testing | ⏳ Not Started | Large files, bad formats |
| 🔲 GitHub Actions CI | ⏳ Not Started | Auto-run tests on push |
| 🔲 Create test suite folder | ⏳ Not Started | /tests/ directory |

---

## 📊 Phase 6: Monitoring & Logs

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Add logging system | ⏳ Not Started | Log file + console |
| 🔲 Integrate Sentry | ⏳ Not Started | Catch crashes & issues |
| 🔲 Optional: Prometheus + Grafana | ⏳ Not Started | Performance metrics |

---

## 🎨 Phase 7: Frontend (Optional)

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Build frontend interface | ⏳ Not Started | React/Vite or HTML |
| 🔲 Upload progress + messages | ⏳ Not Started | Better UX |
| 🔲 Download link system | ⏳ Not Started | Result sharing |

---

## 🔐 Phase 8: User Authentication (Optional)

| Task | Status | Notes |
|------|--------|-------|
| 🔲 Add login/signup endpoints | ⏳ Not Started | JWT or OAuth |
| 🔲 Track user file history | ⏳ Not Started | Optional feature |
| 🔲 Apply quotas per user | ⏳ Not Started | Prevent misuse |

---

## 📁 Folder Structure (Target)
---

## ✅ Summary

- **✅ Completed:** 9 core tasks
- **⏳ In Progress:** 2 tasks
- **🔲 Remaining:** 29+ tasks to go
- This checklist will evolve as the project grows.
