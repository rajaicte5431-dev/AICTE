"""
Pydantic request/response schemas for all API endpoints
"""
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, List


# ── Request models ──────────────────────────────────────────────────────────

class AnalyzeSyllabusRequest(BaseModel):
    syllabus_text: str = Field(..., min_length=20, description="Raw syllabus content to analyse")
    course_level: Optional[str] = Field(default="undergraduate", description="undergraduate | postgraduate | doctoral")
    accreditation_body: Optional[str] = Field(default="ABET", description="ABET | NAAC | NBA | Other")


class GenerateSyllabusRequest(BaseModel):
    course_title: str = Field(..., description="Name of the course")
    course_description: str = Field(..., description="Brief course description")
    duration_weeks: int = Field(default=15, ge=4, le=52)
    credits: int = Field(default=3, ge=1, le=6)
    course_level: Optional[str] = Field(default="undergraduate")
    department: Optional[str] = Field(default="")
    accreditation_body: Optional[str] = Field(default="ABET")
    focus_areas: Optional[List[str]] = Field(default=[])


class MapOutcomesRequest(BaseModel):
    syllabus_text: str = Field(..., description="Full syllabus text")
    accreditation_body: Optional[str] = Field(default="ABET")


class RecommendResourcesRequest(BaseModel):
    course_title: str
    topics: List[str] = Field(..., description="List of topics covered in the course")
    course_level: Optional[str] = Field(default="undergraduate")


class CheckAccreditationRequest(BaseModel):
    syllabus_text: str
    accreditation_body: str = Field(default="ABET", description="ABET | NAAC | NBA")


class OptimizeRequest(BaseModel):
    syllabus_text: str
    optimization_goals: Optional[List[str]] = Field(
        default=["improve_outcomes", "update_resources", "add_assessments"],
        description="Goals for optimisation"
    )


# ── Response models ──────────────────────────────────────────────────────────

class AIResponse(BaseModel):
    status: str = "success"
    result: str
    model_used: str = "ibm/granite-13b-instruct-v2"
    tokens_used: Optional[int] = None
