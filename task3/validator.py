def validate_sql(sql):
    """
    Checks if the SQL query is safe to execute.
    Only SELECT queries are allowed.
    Returns (True, None) if safe, (False, error_message) if not.
    """

    # remove extra spaces and convert to uppercase for checking
    sql_upper = sql.strip().upper()

    # list of dangerous keywords to block
    blocked_keywords = ["DELETE", "DROP", "UPDATE", "INSERT", "ALTER", "TRUNCATE", "CREATE"]

    # check if query starts with SELECT
    if not sql_upper.startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    # check for dangerous keywords anywhere in the query
    for keyword in blocked_keywords:
        if keyword in sql_upper:
            return False, f"Dangerous keyword detected: {keyword}"

    return True, None


# test it directly
if __name__ == "__main__":
    # safe query
    safe = "SELECT * FROM customers"
    print(validate_sql(safe))

    # dangerous query
    dangerous = "DROP TABLE customers"
    print(validate_sql(dangerous))

    # another dangerous one
    dangerous2 = "SELECT * FROM customers; DELETE FROM customers"
    print(validate_sql(dangerous2))