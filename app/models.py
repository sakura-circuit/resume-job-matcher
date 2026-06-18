from pydantic import BaseModel

class MatchResponse(BaseModel):
    score: float
    matching_skills: list[str]
    missing_skills: list[str]