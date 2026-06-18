import json
import re
import os

from ollama import chat

from app.prompt_builder import build_prompt

MODEL_NAME = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:7b"
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

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return extract_json(
        response["message"]["content"]
    )