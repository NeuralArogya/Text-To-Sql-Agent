# Task 4 – Mini SQL Agent (FastAPI)

A FastAPI-powered agentic system that takes natural language questions via API and returns SQL results with natural language summaries.

---

## Files

- `main.py` — FastAPI app with /agent/sql endpoint
- `agent.py` — core agent logic with retry up to 3 times
- `logs/` — stores agent execution logs

---

## How to run

```bash
uvicorn task4.main:app --reload
```

Then open:
- `http://127.0.0.1:8000` — check if API is running
- `http://127.0.0.1:8000/docs` — interactive API docs to test

---

## API Usage

**Endpoint:** `POST /agent/sql`

**Input:**
```json
{
    "question": "How many customers are from USA?"
}
```

**Output:**
```json
{
    "question": "How many customers are from USA?",
    "sql": "SELECT COUNT(\"customerNumber\") FROM customers WHERE \"country\" = 'USA'",
    "result": 36,
    "summary": "There are 36 customers from the USA.",
    "status": "success",
    "execution_time": 0.717,
    "attempts": 1
}
```

---

## Agent Flow
Question received
↓
Generate SQL using Groq AI
↓
Validate SQL safety
↓
Execute on PostgreSQL
↓
If fails → fix and retry (max 3 times)
↓
Generate natural language summary
↓
Return structured response