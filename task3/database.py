import psycopg2
import os
from dotenv import load_dotenv

# reads your .env file
load_dotenv()

def get_connection():
    """Create and return a PostgreSQL database connection"""
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None


def test_connection():
    """Test if the database connection works"""
    conn = get_connection()
    if conn:
        print("Database connected successfully!")
        conn.close()
    else:
        print("Database connection failed!")


# this runs only when you run database.py directly
if __name__ == "__main__":
    test_connection()