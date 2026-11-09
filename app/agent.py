"""
Core AI agent — builds prompts and orchestrates IBM Granite calls
for all curriculum-design tasks.
"""
from __future__ import annotations
from app.granite_client import granite_generate
from app.schemas import (
    AnalyzeSyllabusRequest,
    GenerateSyllabusRequest,
    MapOutcomesRequest,
    RecommendResourcesRequest,
    CheckAccreditationRequest,
    OptimizeRequest,
)


# ── Prompts ──────────────────────────────────────────────────────────────────

def _analyze_prompt(req: AnalyzeSyllabusRequest) -> str:
    return (
        f"You are an expert academic curriculum designer and accreditation specialist.\n"
        f"Accreditation body: {req.accreditation_body}\n"
        f"Course level: {req.course_level}\n\n"
        f"Carefully analyze the following syllabus and provide:\n"
        f"1. Strengths of the current syllabus\n"
        f"2. Identified gaps and weaknesses\n"
        f"3. Specific, actionable recommendations aligned with {req.accreditation_body} standards\n"
        f"4. Suggestions to improve learning outcomes using Bloom's Taxonomy\n\n"
        f"SYLLABUS:\n{req.syllabus_text}\n\n"
        f"Provide a structured, detailed analysis:"
    )


def _generate_prompt(req: GenerateSyllabusRequest) -> str:
    focus = ", ".join(req.focus_areas) if req.focus_areas else "general topics"
    return (
        f"You are an expert curriculum designer. Generate a complete, professional course syllabus.\n\n"
        f"Course Title: {req.course_title}\n"
        f"Department: {req.department}\n"
        f"Description: {req.course_description}\n"
        f"Duration: {req.duration_weeks} weeks | Credits: {req.credits}\n"
        f"Level: {req.course_level}\n"
        f"Accreditation: {req.accreditation_body}\n"
        f"Focus Areas: {focus}\n\n"
        f"Generate a complete syllabus including:\n"
        f"- Course description\n"
        f"- Measurable learning outcomes (Bloom's Taxonomy levels)\n"
        f"- Week-by-week schedule with topics and assessments\n"
        f"- Assessment breakdown with percentages\n"
        f"- Required and recommended resources\n"
        f"- Alignment with {req.accreditation_body} student outcomes\n\n"
        f"SYLLABUS:"
    )


def _outcomes_prompt(req: MapOutcomesRequest) -> str:
    return (
        f"You are a curriculum mapping expert specializing in {req.accreditation_body} accreditation.\n\n"
        f"Map the learning outcomes from the syllabus below to:\n"
        f"1. Bloom's Taxonomy cognitive levels\n"
        f"2. Specific assessments\n"
        f"3. {req.accreditation_body} student outcomes / criteria\n\n"
        f"Present the mapping as a clear table and include gap analysis.\n\n"
        f"SYLLABUS:\n{req.syllabus_text}\n\n"
        f"OUTCOME MAPPING:"
    )


def _resources_prompt(req: RecommendResourcesRequest) -> str:
    topics_str = "\n".join(f"- {t}" for t in req.topics)
    return (
        f"You are an academic librarian and curriculum specialist.\n\n"
        f"Course: {req.course_title} ({req.course_level})\n"
        f"Topics covered:\n{topics_str}\n\n"
        f"Recommend:\n"
        f"1. Primary textbooks (prefer editions from 2020–2025)\n"
        f"2. Recent peer-reviewed articles (IEEE, ACM, Springer)\n"
        f"3. Online platforms and MOOCs\n"
        f"4. Industry reports and white papers\n"
        f"5. IBM Skills Network / open courseware resources\n\n"
        f"RECOMMENDED RESOURCES:"
    )


def _accreditation_prompt(req: CheckAccreditationRequest) -> str:
    return (
        f"You are an {req.accreditation_body} accreditation auditor.\n\n"
        f"Review the following syllabus and:\n"
        f"1. Map each section to specific {req.accreditation_body} criteria/student outcomes\n"
        f"2. Identify which criteria are fully met, partially met, or missing\n"
        f"3. Provide a compliance score (0–100%) per criterion\n"
        f"4. List concrete steps to achieve full compliance\n\n"
        f"SYLLABUS:\n{req.syllabus_text}\n\n"
        f"{req.accreditation_body} COMPLIANCE REPORT:"
    )


def _optimize_prompt(req: OptimizeRequest) -> str:
    goals_str = "\n".join(f"- {g.replace('_', ' ').title()}" for g in req.optimization_goals)
    return (
        f"You are a senior curriculum designer with expertise in academic quality assurance.\n\n"
        f"Optimization Goals:\n{goals_str}\n\n"
        f"Analyze the syllabus below and return an optimized, improved version that addresses "
        f"all the stated goals. Include a change-log summarizing what was changed and why.\n\n"
        f"ORIGINAL SYLLABUS:\n{req.syllabus_text}\n\n"
        f"OPTIMIZED SYLLABUS:"
    )


# ── Agent functions ──────────────────────────────────────────────────────────

def analyze_syllabus(req: AnalyzeSyllabusRequest) -> str:
    return granite_generate(_analyze_prompt(req))


def generate_syllabus(req: GenerateSyllabusRequest) -> str:
    return granite_generate(_generate_prompt(req))


def map_outcomes(req: MapOutcomesRequest) -> str:
    return granite_generate(_outcomes_prompt(req))


def recommend_resources(req: RecommendResourcesRequest) -> str:
    return granite_generate(_resources_prompt(req))


def check_accreditation(req: CheckAccreditationRequest) -> str:
    return granite_generate(_accreditation_prompt(req))


def optimize_syllabus(req: OptimizeRequest) -> str:
    return granite_generate(_optimize_prompt(req))
