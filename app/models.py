from pydantic import BaseModel

class MatchResponse(BaseModel):
    score: float
    matching_skills: list[str]
    missing_skills: list[str]

class AIAnalysisResponse(BaseModel):
    match_score: int
    reasoning: str
    strengths: list[str]
    missing_skills: list[str]
    recommendations: list[str]