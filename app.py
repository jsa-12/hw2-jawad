import os
import sys

from google import genai
from google.genai import types


SUPPORT_PROMPT = """Write a polite and professional customer support reply in under 120 words.
Acknowledge the issue, ask for missing information if necessary, and suggest next steps.
Do not invent policies. Escalate legal or refund disputes to a human agent.
"""

MODEL_NAME = "gemini-2.5-flash"


def get_customer_message() -> str:
    if len(sys.argv) < 2:
        print('Usage: python app.py "Customer message here"', file=sys.stderr)
        sys.exit(1)
    return " ".join(sys.argv[1:]).strip()


def get_api_key() -> str:
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(
            "Error: set GOOGLE_API_KEY or GEMINI_API_KEY before running this script.",
            file=sys.stderr,
        )
        sys.exit(1)
    return api_key


def main() -> None:
    customer_message = get_customer_message()
    api_key = get_api_key()

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=customer_message,
            config=types.GenerateContentConfig(
                system_instruction=SUPPORT_PROMPT,
                max_output_tokens=200,
            ),
        )
    except Exception as exc:
        print(f"Gemini API request failed: {exc}", file=sys.stderr)
        sys.exit(1)

    if not response.text:
        print("Gemini API returned an empty response.", file=sys.stderr)
        sys.exit(1)

for part in response.candidates[0].content.parts:
    print(part.text, end="")
    print()

if __name__ == "__main__":
    main()
