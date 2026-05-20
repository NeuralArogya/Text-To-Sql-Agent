# Task 3 – Text-to-SQL Pipeline

A Python pipeline that converts natural language questions into SQL queries and executes them on a PostgreSQL database using Groq AI.

---

## Files

- `database.py` — connects to PostgreSQL
- `sql_generator.py` — sends question to Groq AI and gets SQL back
- `validator.py` — blocks dangerous queries like DELETE/DROP
- `executor.py` — runs SQL on the database with retry logic
- `main.py` — interactive mode, type your own questions
- `benchmark.py` — runs all 50 benchmark questions automatically
- `logs/` — stores benchmark results

---

## How to run

**Interactive mode:**
```bash
python3 task3/main.py
```

**Benchmark mode:**
```bash
python3 task3/benchmark.py
```

---

## Benchmark Results
- Total Questions: 50
- Success Rate: 100%
- Retry Needed: 0

---

## Pipeline Flow
```
Natural Language Question
        ↓
Groq AI generates SQL
        ↓
Validator checks safety
        ↓
Executor runs on PostgreSQL
        ↓
Results returned
```