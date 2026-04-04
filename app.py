import os
from google import genai

customer_message = "Hi, my order arrived damaged. Can I get a replacement?"

prompt = """
Write a polite and professional customer support reply in under 120 words.
Acknowledge the issue, apologize when appropriate, and suggest next steps.
Do not invent company policies.
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{prompt}\n\nCustomer message:\n{customer_message}"
)

print("Customer Message:")
print(customer_message)

print("\nAI Response:")
print(response.text)
