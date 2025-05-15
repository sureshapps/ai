# GPT Social Media Post Generator

## Features
- Single-page app
- GPT-3.5 powered short post generator

## Setup

1. Clone the repo and `cd` into it.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your OpenAI API Key:
```bash
export OPENAI_API_KEY=your-api-key
```

4. Run the app:
```bash
uvicorn main:app --reload
```

5. Visit: `http://localhost:8000`
