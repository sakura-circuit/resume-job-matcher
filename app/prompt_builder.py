def build_prompt(
    resume_text: str,
    job_text: str
) -> str:

    return f"""
You are an experienced technical recruiter.

Analyze how well the candidate matches the job.

Rules:

- Match score must be between 0 and 100.
- Explain WHY the score was assigned.
- Always provide at least 2 recommendations.
- Recommendations must be actionable.

Return ONLY valid JSON.

Schema:

{{
    "match_score": 0,
    "reasoning": "",
    "strengths": [],
    "missing_skills": [],
    "recommendations": []
}}

Resume:
{resume_text}

Job Description:
{job_text}
"""