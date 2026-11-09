"""
File parsing utilities — extract text from uploaded PDF / DOCX / TXT files
"""
from __future__ import annotations
import io
from pathlib import Path


def extract_text(file_bytes: bytes, filename: str) -> str:
    """Return plain text extracted from a PDF, DOCX, or TXT file."""
    suffix = Path(filename).suffix.lower()

    if suffix == ".pdf":
        return _extract_pdf(file_bytes)
    elif suffix in (".docx", ".doc"):
        return _extract_docx(file_bytes)
    elif suffix == ".txt":
        return file_bytes.decode("utf-8", errors="replace")
    else:
        raise ValueError(f"Unsupported file type: {suffix}. Please upload PDF, DOCX, or TXT.")


def _extract_pdf(data: bytes) -> str:
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(data))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages).strip()
    except Exception as exc:
        raise RuntimeError(f"Could not parse PDF: {exc}") from exc


def _extract_docx(data: bytes) -> str:
    try:
        from docx import Document
        doc = Document(io.BytesIO(data))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)
    except Exception as exc:
        raise RuntimeError(f"Could not parse DOCX: {exc}") from exc
