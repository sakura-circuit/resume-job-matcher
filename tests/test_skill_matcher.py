from app.skill_matcher import (
    extract_skills,
    calculate_match_score
)

def test_extract_skills():

    text = """
    Python FastAPI Docker SQL
    """

    result = extract_skills(text)

    assert "python" in result
    assert "docker" in result

def test_match_score():

    resume = {"python", "docker"}

    job = {"python", "docker", "aws"}

    score = calculate_match_score(
        resume,
        job
    )

    assert score == 66.67