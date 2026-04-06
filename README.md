# HW2 – Simple GenAI Workflow

## Project Title
HW2 – Simple GenAI Workflow

## Business Workflow
I chose a customer support response drafting workflow.

## User
The user is a customer support employee.

## Input
The system receives a customer message, complaint, or request.

## Output
The system produces a professional draft reply that acknowledges the issue and suggests next steps.

## Why This Is Valuable
Customer support teams often repeat similar writing tasks. Automating the first draft can save time, improve consistency, and help staff respond more efficiently.

## Files in the Repository
- `app.py`: The final Gemini script that takes a customer message and generates a draft support reply.
- `prompts.md`: Shows the prompt iteration process, including the initial prompt, Revision 1, Revision 2, what changed, and what improved.
- `eval_set.md`: Contains 5 test cases used to evaluate the quality and safety of the prompt.
- `report.md`: A short report describing the use case, model choice, prompt improvements, limitations, and recommendation.
- `README.md`: Explains the project workflow, what each file does, and how to run the script.

## How to Run
1. Install the Gemini Python package:

```bash
pip3 install google-genai
```

2. Set your Gemini API key:

```bash
export GEMINI_API_KEY="your_key_here"
```

3. Run the script with a sample customer message:

```bash
python3 app.py "My order arrived damaged. Can I get a replacement?"
```
## Demo Video

You can watch the demo of the project here:

https://youtu.be/YOUR_VIDEO_LINK
```
