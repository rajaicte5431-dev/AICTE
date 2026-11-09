"""
FastAPI route definitions for the Syllabus & Curriculum Design Optimizer
"""
from __future__ import annotations

from fastapi import APIRouter, UploadFile, File, HTTPException
from app import agent
from app.schemas import (
    AnalyzeSyllabusRequest,
    GenerateSyllabusRequest,
    MapOutcomesRequest,
    RecommendResourcesRequest,
    CheckAccreditationRequest,
    OptimizeRequest,
    AIResponse,
)
from app.file_parser import extract_text
from app.config import settings

router = APIRouter()


# ── Health ──────────────────────────────────────────────────────────────────

@router.get("/health")
def health():
    return {"status": "ok", "app": settings.APP_NAME, "model": settings.GRANITE_MODEL_ID}


# ── Upload & extract ─────────────────────────────────────────────────────────

@router.post("/upload-syllabus", response_model=dict)
async def upload_syllabus(file: UploadFile = File(...)):
    """Upload a PDF/DOCX/TXT syllabus file and return its extracted text."""
    max_bytes = settings.MAX_FILE_SIZE_MB * 1024 * 1024
    content = await file.read()
    if len(content) > max_bytes:
        raise HTTPException(status_code=413, detail=f"File exceeds {settings.MAX_FILE_SIZE_MB} MB limit.")
    try:
        text = extract_text(content, file.filename or "upload.txt")
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {"filename": file.filename, "characters": len(text), "text": text}


# ── Core AI endpoints ─────────────────────────────────────────────────────────

@router.post("/analyze", response_model=AIResponse)
def analyze(req: AnalyzeSyllabusRequest):
    """Analyze an existing syllabus and surface improvements."""
    result = agent.analyze_syllabus(req)
    return AIResponse(result=result, model_used=settings.GRANITE_MODEL_ID)


@router.post("/generate", response_model=AIResponse)
def generate(req: GenerateSyllabusRequest):
    """Generate a new syllabus from scratch."""
    result = agent.generate_syllabus(req)
    return AIResponse(result=result, model_used=settings.GRANITE_MODEL_ID)


@router.post("/map-outcomes", response_model=AIResponse)
def map_outcomes(req: MapOutcomesRequest):
    """Map learning outcomes to Bloom's Taxonomy and accreditation standards."""
    result = agent.map_outcomes(req)
    return AIResponse(result=result, model_used=settings.GRANITE_MODEL_ID)


@router.post("/recommend-resources", response_model=AIResponse)
def recommend_resources(req: RecommendResourcesRequest):
    """Recommend textbooks, articles and online resources for a course."""
    result = agent.recommend_resources(req)
    return AIResponse(result=result, model_used=settings.GRANITE_MODEL_ID)


@router.post("/check-accreditation", response_model=AIResponse)
def check_accreditation(req: CheckAccreditationRequest):
    """Check syllabus alignment against ABET / NAAC / NBA standards."""
    result = agent.check_accreditation(req)
    return AIResponse(result=result, model_used=settings.GRANITE_MODEL_ID)


@router.post("/optimize", response_model=AIResponse)
def optimize(req: OptimizeRequest):
    """Return an optimized version of the syllabus with a change-log."""
    result = agent.optimize_syllabus(req)
    return AIResponse(result=result, model_used=settings.GRANITE_MODEL_ID)
