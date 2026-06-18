from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

from app.models import MatchResponse
from app.pdf_reader import extract_text
from app.skill_matcher import (
    calculate_match_score,
    extract_skills,
    get_matching_skills,
    get_missing_skills
)

from app.ai_analyzer import analyze_resume
from app.models import AIAnalysisResponse


app = FastAPI()

@app.get("/")
def root():

    return {
        "project": "Resume Job Matcher",
        "status": "running"
    }

@app.post(
    "/match",
    response_model=MatchResponse
)
async def match_resume(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    
    # Save uploaded PDF temporarily

    with NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:
        
        content = await resume.read()
        temp_file.write(content)

        pdf_path = temp_file.name

    try:

        resume_text = extract_text(pdf_path)

        job_text = (
            await job_description.read()
        ).decode("utf-8")

        resume_skills = extract_skills(resume_text)

        job_skills = extract_skills(job_text)

        matching = get_matching_skills(resume_skills, job_skills)

        missing = get_missing_skills(resume_skills, job_skills)

        score = calculate_match_score(resume_skills, job_skills)

        return MatchResponse(
            score=score,
            matching_skills=sorted(list(matching)),
            missing_skills=sorted(list(missing))
        )
    
    finally:
        Path(pdf_path).unlink(
            missing_ok=True
        )


@app.post(
    "/ai-match",
    response_model=AIAnalysisResponse
)
async def ai_match_resume(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    
    with NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:
        
        temp_file.write(
            await resume.read()
        )

        pdf_path = temp_file.name

    try:

        resume_text = extract_text(
            pdf_path
        )

        job_text = (
            await job_description.read()
        ).decode("utf-8")

        analysis = analyze_resume(
            resume_text,
            job_text
        )

        return AIAnalysisResponse(
            **analysis
        )
    
    finally:
        Path(pdf_path).unlink(
            missing_ok=True
        )