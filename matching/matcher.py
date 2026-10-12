
import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
JOBS_FILE = PROJECT_DIR / "data" / "sample_jobs.csv"


def calculate_match(resume_skills, required_skills):
    resume_skills = {
        skill.strip().lower() for skill in resume_skills
    }

    required_skills = [
        skill.strip() for skill in required_skills
    ]

    matched = [
        skill for skill in required_skills
        if skill.lower() in resume_skills
    ]

    missing = [
        skill for skill in required_skills
        if skill.lower() not in resume_skills
    ]

    if not required_skills:
        score = 0
    else:
        score = round(
            len(matched) / len(required_skills) * 100
        )

    return score, matched, missing


def main():
    resume_skills = [
        "Python", "SQL", "Git",
        "HTML", "CSS", "JavaScript"
    ]

    print("AI RESUME & JOB MATCHING AGENT")
    print("=" * 35)

    with open(
        JOBS_FILE, "r", encoding="utf-8", newline=""
    ) as file:
        jobs = csv.DictReader(file)

        for job in jobs:
            required_skills = (
                job["required_skills"].split(";")
            )

            score, matched, missing = calculate_match(
                resume_skills, required_skills
            )

            print(f"\nJob: {job['title']}")
            print(f"Match score: {score}%")
            print("Matched skills:", ", ".join(matched) or "None")
            print("Missing skills:", ", ".join(missing) or "None")


if __name__ == "__main__":
    main()
