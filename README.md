# Resume ↔ Job Matcher

## Overview

**Resume ↔ Job Matcher** is an AI-powered application that compares a candidate's resume with a job description and generates a compatibility score along with actionable recommendations.

---

## Project Goal

The objective is to build a production-style application that helps candidates understand how well their resume matches a specific job posting.

### Features

- Upload Resume (PDF)
- Upload Job Description (TXT or PDF)
- Extract and process text
- Identify and compare skills
- Calculate a match score
- Generate AI-powered recommendations using an LLM
- Return structured JSON responses
- Expose functionality through a FastAPI REST API

---

## Project Structure

```text
resume-job-matcher/
│
├── app/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── skill_matcher.py
│   └── models.py
│
├── tests/
│   └── test_skill_matcher.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-job-matcher.git

cd resume-job-matcher
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

#### Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pdfplumber pytest
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

## Technology Stack

| Category         | Technology                        |
| ---------------- | --------------------------------- |
| Language         | Python 3.11+                      |
| API Framework    | FastAPI                           |
| PDF Processing   | pdfplumber                        |
| Testing          | pytest                            |
| Server           | Uvicorn                           |
| AI Integration   | OpenAI / Local LLM (future phase) |
| Containerization | Docker (future phase)             |

---

## Example Workflow

1. Upload a resume PDF
2. Upload a job description
3. Extract text from both documents
4. Identify relevant skills and keywords
5. Compute similarity score
6. Generate AI recommendations
7. Return structured JSON output

Example response:

```json
{
  "match_score": 82,
  "matching_skills": ["Python", "FastAPI", "Docker"],
  "missing_skills": ["Kubernetes", "AWS"],
  "recommendations": [
    "Add cloud experience examples",
    "Highlight containerization projects"
  ]
}
```

---

## Testing

Run unit tests:

```bash
pytest
```

---
