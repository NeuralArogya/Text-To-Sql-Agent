import json
import os
from sql_generator import generate_sql
from executor import execute_sql


# all 50 benchmark questions
QUESTIONS = [
    "List all products",
    "Get all customers",
    "Show all orders",
    "List all employees",
    "Get all offices",
    "Show all product lines",
    "List all payments",
    "Get product names and prices",
    "Get customer names and cities",
    "List employee first and last names",
    "Get all order dates",
    "Show product vendor list",
    "Get all product codes",
    "List all countries from offices",
    "Show all order statuses",
    "Get all payment amounts",
    "List all job titles",
    "Get customer phone numbers",
    "Show product MSRP values",
    "List order numbers",
    "Get orders with customer names",
    "Get employees with office city",
    "Get payments with customer names",
    "Get order details with product names",
    "Get products with product line description",
    "Get customers with sales rep names",
    "Get orders with customer city",
    "Get employees and their manager",
    "Get orderdetails with product vendor",
    "Get payments with customer country",
    "Count customers per country",
    "Total payments per customer",
    "Number of orders per status",
    "Products per product line",
    "Employees per office",
    "Total stock per product vendor",
    "Average buy price per product line",
    "Orders per customer",
    "Max MSRP per product line",
    "Min buy price per vendor",
    "Total number of customers",
    "Total number of products",
    "Total revenue from payments",
    "Average product price",
    "Max payment amount",
    "Min payment amount",
    "Count total orders",
    "Total quantity in stock",
    "Average MSRP",
    "Number of employees"
]


def run_benchmark():
    """
    Runs all 50 benchmark questions through the Text-to-SQL pipeline
    and saves a full evaluation report
    """

    # make sure logs folder exists
    os.makedirs("logs", exist_ok=True)

    total = len(QUESTIONS)
    success_count = 0
    failed_count = 0
    retry_count = 0
    results_log = []

    print("=" * 60)
    print("BENCHMARK EVALUATION — ALL 50 QUESTIONS")
    print("=" * 60)

    for i, question in enumerate(QUESTIONS, 1):
        print(f"\n[{i}/{total}] {question}")

        # step 1: generate sql
        sql = generate_sql(question)

        if not sql:
            print("❌ FAILED — SQL generation returned nothing")
            failed_count += 1
            results_log.append({
                "question_number": i,
                "question": question,
                "generated_sql": None,
                "status": "failed",
                "error": "SQL generation failed",
                "rows_returned": 0,
                "execution_time": None,
                "attempts": 0,
                "retry_needed": False
            })
            continue

        # step 2: execute sql
        result = execute_sql(sql)

        # step 3: track results
        status = result.get("status")
        attempts = result.get("attempts", 1)
        retry_needed = attempts > 1

        if status == "success":
            success_count += 1
            rows = result.get("result", [])
            print(f"✅ SUCCESS — {len(rows)} rows — {result.get('execution_time')}s", end="")
            if retry_needed:
                retry_count += 1
                print(f" (needed retry)", end="")
            print()
        else:
            failed_count += 1
            print(f"❌ FAILED — {result.get('error')}")

        results_log.append({
            "question_number": i,
            "question": question,
            "generated_sql": sql,
            "status": status,
            "error": result.get("error"),
            "rows_returned": len(result.get("result") or []),
            "execution_time": result.get("execution_time"),
            "attempts": attempts,
            "retry_needed": retry_needed
        })

    # print summary
    print("\n" + "=" * 60)
    print("BENCHMARK SUMMARY REPORT")
    print("=" * 60)
    print(f"Total Questions    : {total}")
    print(f"Successful         : {success_count}")
    print(f"Failed             : {failed_count}")
    print(f"Needed Retry       : {retry_count}")
    print(f"Success Rate       : {round(success_count / total * 100, 1)}%")
    print("=" * 60)

    # save full report to json
    report = {
        "summary": {
            "total_questions": total,
            "successful": success_count,
            "failed": failed_count,
            "needed_retry": retry_count,
            "success_rate": f"{round(success_count / total * 100, 1)}%"
        },
        "results": results_log
    }

    with open("logs/benchmark_results.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    print("\nFull report saved to logs/benchmark_results.json")


if __name__ == "__main__":
    run_benchmark()