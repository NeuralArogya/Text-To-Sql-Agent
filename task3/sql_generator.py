import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# initialize groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# this tells groq exactly what kind of SQL to generate
SYSTEM_PROMPT = """
You are an expert SQL generator for a PostgreSQL database called ClassicModels.

The database has these tables and columns:

- products: "productCode", "productName", "productLine", "productScale", "productVendor", "productDescription", "quantityInStock", "buyPrice", "MSRP"
- customers: "customerNumber", "customerName", "contactLastName", "contactFirstName", "phone", "addressLine1", "addressLine2", "city", "state", "postalCode", "country", "salesRepEmployeeNumber", "creditLimit"
- orders: "orderNumber", "orderDate", "requiredDate", "shippedDate", "status", "comments", "customerNumber"
- orderdetails: "orderNumber", "productCode", "quantityOrdered", "priceEach", "orderLineNumber"
- employees: "employeeNumber", "lastName", "firstName", "extension", "email", "officeCode", "reportsTo", "jobTitle"
- offices: "officeCode", "city", "phone", "addressLine1", "addressLine2", "state", "country", "postalCode", "territory"
- payments: "customerNumber", "checkNumber", "paymentDate", "amount"
- productlines: "productLine", "textDescription", "htmlDescription", "image"

IMPORTANT RULES:
1. Always wrap column names in double quotes like "columnName"
2. Only generate SELECT queries
3. Return ONLY the SQL query — no explanation, no markdown, no backticks
4. Use proper JOINs when multiple tables are needed
"""


def generate_sql(question):
    """
    Sends a natural language question to Groq and returns a SQL query.
    """
    try:
        print(f"Generating SQL for: {question}")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Generate a SQL query for: {question}"}
            ],
            temperature=0,
            max_tokens=500
        )

        # extract the sql from the response
        sql = response.choices[0].message.content.strip()

        print(f"Generated SQL: {sql}")
        return sql

    except Exception as e:
        print(f"SQL generation failed: {e}")
        return None


# test it directly
if __name__ == "__main__":
    questions = [
        "List all products",
        "Count customers per country",
        "Get orders with customer names"
    ]

    for q in questions:
        print(f"\nQuestion: {q}")
        sql = generate_sql(q)
        print(f"SQL: {sql}")
        print("-" * 50)