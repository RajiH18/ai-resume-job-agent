import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
JOBS_FILE = PROJECT_DIR / "data" / "sample_jobs.csv"


def normalize_skill(skill):
    """Normalize skill names for comparison."""
    skill = skill.strip().lower()
    aliases = {
        "powerbi": "power bi",
        "rest api": "rest api",
        "ml": "machine learning",
    }
    return aliases.get(skill, skill)


def calculate_match(resume_skills, required_skills):
    resume_skills = {
        normalize_skill(skill)
        for skill in resume_skills
        if skill.strip()
    }

    required_skills = [
        skill.strip()
        for skill in required_skills
        if skill.strip()
    ]

    matched = [
        skill for skill in required_skills
        if normalize_skill(skill) in resume_skills
    ]

    missing = [
        skill for skill in required_skills
        if normalize_skill(skill) not in resume_skills
    ]

    score = (
        round(len(matched) / len(required_skills) * 100)
        if required_skills else 0
    )

    return score, matched, missing


def main():
    print("AI RESUME & JOB MATCHING AGENT")
    print("=" * 35)

    user_input = input(
        "\nEnter your skills separated by commas:\n"
    )
    resume_skills = user_input.split(",")

    results = []

    with open(JOBS_FILE, "r", encoding="utf-8", newline="") as file:
        for job in csv.DictReader(file):
            required_skills = job["required_skills"].split(";")

            score, matched, missing = calculate_match(
                resume_skills, required_skills
            )

            results.append({
                "title": job["title"],
                "score": score,
                "matched": matched,
                "missing": missing,
            })

            print(f"\nJob: {job['title']}")
            print(f"Match score: {score}%")
            print("Matched skills:", ", ".join(matched) or "None")
            print("Missing skills:", ", ".join(missing) or "None")

    if not results:
        print("\nNo jobs found in the dataset.")
        return

    best_job = max(results, key=lambda job: job["score"])

    print("\n" + "=" * 35)
    print("BEST MATCHING JOB RECOMMENDATION")
    print("=" * 35)
    print(f"Recommended job: {best_job['title']}")
    print(f"Match score: {best_job['score']}%")

    if best_job["missing"]:
        print("Skills to learn next:", ", ".join(best_job["missing"]))
    else:
        print("You match all listed skills for this job!")


if __name__ == "__main__":
    main()