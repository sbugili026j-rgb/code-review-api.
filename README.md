# Code Review API

An API that reviews code snippets using an AI model. Send it code and it returns a list of issues with a severity, a message and a suggested fix.

Built with Python and FastAPI.

## Run it

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080

Set your OpenAI key as an environment variable named OPENAI_API_KEY (on Replit, add it under Secrets).

Then open /docs in your browser to try it.

## Endpoints

GET /health
Returns {"status": "ok"}

POST /review
Send: {"code": "def add(a, b): return a - b"}
Get back a list of issues, each with severity, message and suggestion.

## Tech

Python, FastAPI, Uvicorn, OpenAI API