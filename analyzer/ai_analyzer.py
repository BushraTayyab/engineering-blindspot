import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def generate_insight(report):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a senior software engineer performing a code-change impact review.

Engineering Blindspot has already analyzed a Git repository and produced
the following deterministic evidence:

{report}

Based ONLY on this evidence:

1. Summarize what changed.
2. Identify the most important potential impact.
3. Identify anything the developer might overlook.
4. Recommend specific checks before merging.

Do not invent files, functions, dependencies, tests, or behavior.
If the evidence is insufficient, explicitly say so.

Return concise, practical engineering advice.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

if __name__ == "__main__":
    from analyzer.impact_analyzer import analyze_impact
    from analyzer.report_analyzer import generate_report

    impact = analyze_impact("../blindspot-demo-orders")
    report = generate_report(impact)

    insight = generate_insight(report)

    print("\n===== ENGINEERING BLINDSPOT =====\n")
    print(insight)