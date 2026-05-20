import sys
import os
import time
import logging

# this lets task4 access task3 files
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'task3'))

from sql_generator import generate_sql
from executor import execute_sql
from validator import validate_sql

# setup logging
os.makedirs("task4/logs", exist_ok=True)
logging.basicConfig(
    filename="task4/logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_summary(question, result):
    """
    Converts SQL result into a human readable natural language summary
    """
    from groq import Groq
    from dotenv import load_dotenv
    load_dotenv()

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
    The user asked: "{question}"
    The SQL query returned this result: {result}
    
    Write a single short sentence summarizing the answer in plain English.
    Do not mention SQL. Just answer the question naturally.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()


def run_agent(question):
    """
    Full agentic pipeline with retry up to 3 times:
    1. Decompose question
    2. Generate SQL
    3. Execute SQL
    4. Retry up to 3 times if failed
    5. Return natural language summary
    """

    start_time = time.time()
    max_retries = 3
    attempt = 0
    last_error = None
    sql = None

    logging.info(f"New question received: {question}")

    # step 1: decompose and generate sql
    print(f"\nStep 1: Understanding question...")
    logging.info(f"Step 1: Generating SQL for: {question}")

    sql = generate_sql(question)

    if not sql:
        logging.error("SQL generation failed - returned None")
        return {
            "question": question,
            "sql": None,
            "result": None,
            "summary": "Sorry I could not understand your question.",
            "status": "failed",
            "error": "SQL generation failed"
        }

    print(f"Generated SQL: {sql}")
    logging.info(f"Generated SQL: {sql}")

    # step 2: validate
    is_safe, error_message = validate_sql(sql)
    if not is_safe:
        logging.warning(f"SQL blocked by validator: {error_message}")
        return {
            "question": question,
            "sql": sql,
            "result": None,
            "summary": "This query is not allowed.",
            "status": "blocked",
            "error": error_message
        }

    # step 3: execute with retry up to 3 times
    while attempt < max_retries:
        attempt += 1
        print(f"\nStep 2: Executing SQL (attempt {attempt}/{max_retries})...")
        logging.info(f"Execution attempt {attempt} for SQL: {sql}")

        result = execute_sql(sql, retry=False)

        if result["status"] == "success":
            rows = result.get("result", [])
            columns = result.get("columns", [])
            execution_time = result.get("execution_time")

            logging.info(f"Execution successful: {len(rows)} rows in {execution_time}s")

            # format result nicely
            if len(rows) == 1 and len(rows[0]) == 1:
                # single value result like COUNT(*)
                formatted_result = rows[0][0]
            elif len(rows) <= 10:
                # small result set
                formatted_result = [dict(zip(columns, row)) for row in rows]
            else:
                # large result set — just show count
                formatted_result = f"{len(rows)} rows returned"

            # step 4: generate natural language summary
            print(f"\nStep 3: Generating summary...")
            summary = generate_summary(question, formatted_result)
            logging.info(f"Summary generated: {summary}")

            total_time = round(time.time() - start_time, 3)

            return {
                "question": question,
                "sql": sql,
                "result": formatted_result,
                "summary": summary,
                "status": "success",
                "execution_time": total_time,
                "attempts": attempt
            }

        else:
            last_error = result.get("error")
            logging.warning(f"Attempt {attempt} failed: {last_error}")
            print(f"Attempt {attempt} failed: {last_error}")

            if attempt < max_retries:
                print(f"Retrying... asking Groq to fix the SQL")
                logging.info(f"Asking Groq to fix SQL. Error: {last_error}")

                # ask groq to fix the sql
                fix_prompt = f"""
                This SQL query failed with error: {last_error}
                
                Failed SQL: {sql}
                
                Fix the SQL query. Return ONLY the corrected SQL, nothing else.
                Remember to wrap all column names in double quotes.
                """

                from groq import Groq
                from dotenv import load_dotenv
                load_dotenv()

                client = Groq(api_key=os.getenv("GROQ_API_KEY"))
                fix_response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": fix_prompt}
                    ],
                    temperature=0,
                    max_tokens=500
                )

                sql = fix_response.choices[0].message.content.strip()
                logging.info(f"Fixed SQL: {sql}")
                print(f"Fixed SQL: {sql}")

    # all retries exhausted
    logging.error(f"All {max_retries} attempts failed. Last error: {last_error}")
    return {
        "question": question,
        "sql": sql,
        "result": None,
        "summary": "Sorry I could not answer your question after multiple attempts.",
        "status": "failed",
        "error": last_error,
        "attempts": attempt
    }


# test directly
if __name__ == "__main__":
    import json
    result = run_agent("How many customers are from USA?")
    print("\nFinal Output:")
    print(json.dumps(result, indent=2, default=str))