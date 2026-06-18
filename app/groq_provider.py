import json
import os
import re

from groq import Groq

from app.prompt_builder import build_prompt

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

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

    return json.loads(
        match.group(0)
    )

def analyze_resume(
    resume_text: str,
    job_text: str,
) -> dict:

    prompt = build_prompt(
        resume_text,
        job_text,
    )

    response = (
        client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    )

    message = response.choices[0].message

    if not message.content:
        raise ValueError(
            "Groq returned empty content"
        )

    return extract_json(
        message.content
    )