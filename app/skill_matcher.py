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

    return {
        skill
        for skill in SKILLS
        if skill in text
    }

def get_matching_skills(
        resume_skills: set[str],
        job_skills: set[str]
) -> set[str]:
    return resume_skills.intersection(job_skills)

def get_missing_skills(
        resume_skills: set[str],
        job_skills: set[str]
) -> set[str]:
    return job_skills - resume_skills

def calculate_match_score(
        resume_skills: set[str],
        job_skills: set[str]
) -> float:
    
    if not job_skills:
        return 0.0
    
    matches = get_matching_skills(resume_skills, job_skills)

    return round(
        len(matches) / len(job_skills) * 100, 2
    )