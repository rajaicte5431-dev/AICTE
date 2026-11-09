# Syllabus & Curriculum Design Optimizer
### Problem Statement #14 — IBM Granite + IBM Cloud Lite

An AI-powered system that assists faculty in developing and refining academic course content using **IBM Granite** on **IBM watsonx.ai (Cloud Lite)**.

---

## Features

| Tool | Description |
|------|-------------|
| 🔍 **Analyze Syllabus** | Upload/paste a syllabus; get strengths, gaps & recommendations |
| ✨ **Generate Syllabus** | Create a complete, standards-aligned syllabus from scratch |
| 🎯 **Map Outcomes** | Map learning outcomes to Bloom's Taxonomy + ABET/NAAC/NBA |
| 📚 **Recommend Resources** | Curated reading lists and online resources |
| ✅ **Accreditation Check** | Compliance report against ABET, NAAC, or NBA |
| ⚡ **Optimize Syllabus** | AI-driven rewrite with change log |

---

## Technology Stack

- **AI Model**: `ibm/granite-13b-instruct-v2` (IBM watsonx.ai)
- **Platform**: IBM Cloud Lite — IBM watsonx.ai
- **Backend**: Python 3.11+ · FastAPI · Uvicorn
- **SDK**: `ibm-watsonx-ai`
- **File Parsing**: `pypdf` (PDF) · `python-docx` (DOCX)
- **Frontend**: Vanilla HTML/CSS/JS (served by FastAPI)

---

## Project Structure

```
Project/
├── main.py                  # FastAPI app entry point
├── requirements.txt         # Python dependencies
├── .env                     # IBM Cloud credentials (⚠ do not commit)
├── env.txt                  # .env reference/template
├── app/
│   ├── config.py            # Pydantic settings (reads .env)
│   ├── granite_client.py    # IBM Granite API wrapper
│   ├── agent.py             # Prompt builder & AI orchestrator
│   ├── schemas.py           # Request/response Pydantic models
│   ├── file_parser.py       # PDF/DOCX/TXT text extraction
│   └── api/
│       └── routes.py        # FastAPI route definitions
├── static/
│   └── index.html           # Full-featured web UI
└── uploads/                 # Temp directory for uploaded files
```

---

## Quick Start

### 1. IBM Cloud Setup (Free / Lite)

1. Sign up at <https://cloud.ibm.com> (no credit card required for Lite)
2. Create an **IBM watsonx.ai** service instance
3. Generate an **API Key** from *Manage → Access (IAM) → API Keys*
4. Note your **Project ID** from the watsonx.ai project settings

### 2. Configure Environment

Edit `.env` (created automatically):

```env
IBM_WATSONX_API_KEY=<your api key>
IBM_WATSONX_URL=https://us-south.ml.cloud.ibm.com
IBM_WATSONX_PROJECT_ID=<your project id>
```

### 3. Install & Run

```bash
pip install -r requirements.txt
python main.py
```

Open **http://localhost:8000** in your browser.

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET  | `/api/health` | Health check |
| POST | `/api/upload-syllabus` | Upload and extract text from file |
| POST | `/api/analyze` | Analyze an existing syllabus |
| POST | `/api/generate` | Generate a new syllabus |
| POST | `/api/map-outcomes` | Map outcomes to standards |
| POST | `/api/recommend-resources` | Recommend resources |
| POST | `/api/check-accreditation` | Accreditation compliance report |
| POST | `/api/optimize` | Optimize and improve a syllabus |

Interactive docs: **http://localhost:8000/docs**

---

## Supported Accreditation Standards

- **ABET** — Accreditation Board for Engineering and Technology
- **NAAC** — National Assessment and Accreditation Council (India)
- **NBA** — National Board of Accreditation (India)

---

## Notes

- The app works in **demo mode** when IBM credentials are not yet configured — it returns realistic structured mock responses so you can explore every feature immediately.
- Replace `your_ibm_cloud_api_key_here` in `.env` with real credentials to enable live IBM Granite inference.
