# AI Resume & Job Matching Agent

An AI-powered project that helps job seekers compare their skills with job requirements, identify skill gaps, and discover relevant learning opportunities.

## Current Features

- Accepts user skills as comma-separated input.
- Compares skills against sample job listings.
- Calculates a simple skill-match percentage.
- Identifies matched and missing skills.
- Recommends the best-matching job from the sample dataset.
- Normalizes common skill-name variations, such as `PowerBI` and `Power BI`.

## Tech Stack

- Python
- CSV for sample job data
- Git and GitHub

## Project Structure

```text
ai-resume-job-agent/
├── data/
│   └── sample_jobs.csv
├── matching/
│   └── matcher.py
├── .gitignore
└── README.md
```

## Run Locally

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Run the matching engine:

```powershell
python matching/matcher.py
```

Enter your skills separated by commas when prompted.

## Project Status

The current version is a rule-based prototype. Amazon Bedrock and Strands Decider 2B integration, testing, and hackathon submission materials are still in progress.

## Disclaimer

Match scores measure the proportion of listed required skills matched. They do not predict hiring probability.
