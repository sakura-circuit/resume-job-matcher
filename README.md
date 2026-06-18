# Resume Job Matcher

AI-powered resume analysis tool built with FastAPI and Large Language Models (LLMs).

The application supports both local LLMs via Ollama and cloud-hosted LLMs via Groq.

The application compares a candidate's resume against a job description and generates:

- Match score (0-100)
- Strengths
- Missing skills
- Improvement recommendations
- AI-generated reasoning

---

## Features

### Traditional Skill Matching

- PDF resume upload
- Job description upload
- Skill extraction
- Match score calculation
- Missing skill detection

### AI-Powered Analysis

- Resume analysis using local or cloud-hosted LLMs
- Configurable AI provider selection
- Structured JSON output
- Recruiter-style feedback
- Actionable recommendations

---

## Example Response

```json
{
  "match_score": 80,
  "reasoning": "Candidate has strong backend development experience and matches most required skills. AWS and Kubernetes are missing.",
  "strengths": ["Python", "FastAPI", "Docker"],
  "missing_skills": ["AWS", "Kubernetes"],
  "recommendations": ["Add AWS projects", "Learn Kubernetes fundamentals"]
}
```

---

## Technology Stack

- Python 3.12
- FastAPI
- Pydantic
- pdfplumber
- Ollama
- Groq
- Qwen 2.5
- Llama 3.3
- pytest
- Uvicorn

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "project": "Resume Job Matcher",
  "status": "running"
}
```

### Traditional Matching

```http
POST /match
```

Returns:

- Match score
- Matching skills
- Missing skills

### AI Matching

```http
POST /ai-match
```

Returns:

- Match score
- Reasoning
- Strengths
- Missing skills
- Recommendations

---

## Running Locally

### Clone Repository

```bash
git clone <repository-url>
cd resume-job-matcher
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama serve
```

### Download Model

```bash
ollama pull qwen2.5:7b
```

### Start Application

```bash
uvicorn app.main:app --reload
```

### Swagger UI

Open:

http://127.0.0.1:8000/docs

---

## Testing

```bash
pytest
```

---

## Future Improvements

- Docker deployment
- GitHub Actions CI/CD
- Resume scoring history
- Resume-to-job semantic matching using embeddings
- RAG-based job analysis
- Frontend dashboard

---

## Why This Project

This project demonstrates:

- Python backend development
- REST API design
- AI integration
- PDF processing
- Structured LLM outputs
- Testing
- Software architecture

Suitable as a portfolio project for Python Backend, AI Engineer and Generative AI Developer roles.

## Configuration

Create a `.env` file in the project root.

Example:

```env
# AI provider: ollama | groq

AI_PROVIDER=ollama

# Ollama settings
OLLAMA_MODEL=qwen2.5:7b

# Groq settings
GROQ_API_KEY=your_api_key_here
```

### Using Ollama

```env
AI_PROVIDER=ollama
OLLAMA_MODEL=qwen2.5:7b
```

### Using Groq

```env
AI_PROVIDER=groq
GROQ_API_KEY=your_api_key_here
```
