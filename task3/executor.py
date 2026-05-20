import time
from database import get_connection
from validator import validate_sql


def execute_sql(sql, retry=True):
    """
    Validates and executes a SQL query against PostgreSQL.
    Retries once if execution fails.
    Returns a dict with status, results, and any error info.
    """

    # step 1: validate the sql first
    is_safe, error_message = validate_sql(sql)
    if not is_safe:
        return {
            "status": "blocked",
            "sql": sql,
            "result": None,
            "error": error_message
        }

    # step 2: try executing the query
    attempt = 1
    while attempt <= 2:
        try:
            print(f"Attempt {attempt}: Executing SQL...")

            # start timer
            start_time = time.time()

            # connect to database
            conn = get_connection()
            cursor = conn.cursor()

            # run the query
            cursor.execute(sql)
            rows = cursor.fetchall()

            # get column names
            columns = [desc[0] for desc in cursor.description]

            # end timer
            end_time = time.time()
            execution_time = round(end_time - start_time, 3)

            # close connection
            cursor.close()
            conn.close()

            print(f"Query executed successfully in {execution_time}s")

            return {
                "status": "success",
                "sql": sql,
                "columns": columns,
                "result": rows,
                "execution_time": execution_time,
                "attempts": attempt
            }

        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")

            if retry and attempt == 1:
                print("Retrying once...")
                attempt += 1
            else:
                return {
                    "status": "failed",
                    "sql": sql,
                    "result": None,
                    "error": str(e),
                    "attempts": attempt
                }


# test it directly
if __name__ == "__main__":
    # test a valid query
    result = execute_sql('SELECT "customerName", "city" FROM customers LIMIT 5')
    print("\nResult:")
    print("Columns:", result.get("columns"))
    print("Rows:", result.get("result"))
    print("Status:", result.get("status"))
    print("Time:", result.get("execution_time"))