import psycopg2
from psycopg2 import OperationalError


def test_postgresql_connection():
    try:
        # Replace the connection details with your own
        connection = psycopg2.connect(
            database="gilead",
            user="gilead",
            password="gilead",
            host="localhost",
            port="5432",
        )
        connection.close()
        print("Connection to PostgreSQL database successful!")
    except OperationalError as e:
        print(f"Error: {e}")


# Call the function to test the PostgreSQL connection
test_postgresql_connection()
