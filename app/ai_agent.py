import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv
from app.prompts import COVER_LETTER_MATCH_PROMPT

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def match_cover_letter(job_description: str, education: str, cover_letter: str):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
{COVER_LETTER_MATCH_PROMPT}

Job Description:
{job_description}

Candidate Education:
{education}

Cover Letter:
{cover_letter}

Evaluate the cover letter match.
"""

    response = model.generate_content(
        prompt,
        request_options={"timeout": 10}
        )
    
    match = re.search(r"\{.*\}", response.text, re.DOTALL)

    if match:
        return json.loads(match.group())
    
    return {
        "job_description_match": "0%",
        "education_match": "0%",
        "requirements_match": "0%",
        "overall_match": "0%",
        "summary": "AI response could not be parsed."
    }
