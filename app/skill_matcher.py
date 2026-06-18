SKILLS = {
    "python",
    "fastapi",
    "docker",
    "sql",
    "aws",
    "git",
    "linux",
    "kubernetes",
    "javascript",
    "react"
}

def extract_skills(text: str) -> set[str]:
    text = text.lower()

    found = set()

    for skill in SKILLS:
        if skill in text:
            found.add(skill)

    return found

def calculate_match_score(
        resume_skills: set[str],
        job_skills: set[str]
) -> float:
    
    if not job_skills:
        return 0.0
    
    matches = resume_skills.intersection(job_skills)

    return round(
        len(matches) / len(job_skills) * 100, 2
    )