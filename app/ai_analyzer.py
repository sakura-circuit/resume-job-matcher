import os

from dotenv import load_dotenv

load_dotenv()

from app.groq_provider import (
    analyze_resume as groq_analyze
)

from app.ollama_provider import (
    analyze_resume as ollama_analyze
)

def analyze_resume(
    resume_text: str,
    job_text: str,
) -> dict:

    provider = os.getenv(
        "AI_PROVIDER",
        "ollama"
    )

    if provider == "groq":
        return groq_analyze(
            resume_text,
            job_text
        )

    if provider == "ollama":
        return ollama_analyze(
            resume_text,
            job_text
        )

    raise ValueError(
        f"Unknown AI_PROVIDER: {provider}"
    )