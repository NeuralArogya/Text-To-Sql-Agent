import sys
from sql_generator import generate_sql
from executor import execute_sql

def main():
    """
    Main entry point for the Text-to-SQL Generator.
    It takes a natural language question from the user,
    generates SQL, executes it, and displays the results.
    """
    print("--- Text-to-SQL Generator ---")
    print("Ask a question about the ClassicModels database (or type 'exit' to quit)")
    
    while True:
        try:
            # Get user input
            question = input("\nQuestion: ").strip()
            
            if not question:
                continue
            
            if question.lower() in ["exit", "quit", "bye"]:
                print("Goodbye!")
                break
            
            # Step 1: Generate SQL from natural language
            sql = generate_sql(question)
            
            if not sql:
                print("Error: Could not generate SQL for this question.")
                continue
            
            # Step 2: Execute the generated SQL
            result = execute_sql(sql)
            
            # Step 3: Handle the results
            if result["status"] == "success":
                columns = result["columns"]
                rows = result["result"]
                
                if not rows:
                    print("No results found.")
                else:
                    # Print headers
                    header = " | ".join(str(col) for col in columns)
                    print("\n" + header)
                    print("-" * len(header))
                    
                    # Print data rows
                    for row in rows:
                        print(" | ".join(str(val) for val in row))
                
                print(f"\n(Execution time: {result['execution_time']}s)")
                
            elif result["status"] == "blocked":
                print(f"Blocked: {result['error']}")
                
            else:
                print(f"Failed: {result['error']}")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
