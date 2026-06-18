import json
import re

from ollama import chat

def extract_json(content: str) -> dict:

    match = re.search(
        r"\{.*\}",
        content,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            f"No JSON found:\n{content}"
        )

    try:
        return json.loads(
            match.group(0)
        )

    except json.JSONDecodeError as ex:
        raise ValueError(
            f"Invalid JSON:\n{content}"
        ) from ex

def analyze_resume(
        resume_text: str,
        job_text: str
) -> dict:
    
    prompt = f"""
You are an experienced technical recruiter.

Analyze how well the candidate matches the job.

Rules:

- Match score must be between 0 and 100.
- Explain WHY the score was assigned.
- Always provide at least 2 recommendations.
- Recommendations must be actionable.
- Missing required skills should reduce the score.
- Relevant experience should increase the score.

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
    
    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    print("\n===== OLLAMA RAW RESPONSE =====")
    print(content)
    print("==============================\n")

    return extract_json(content)