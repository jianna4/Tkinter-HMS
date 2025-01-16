import mysql.connector
from mysql.connector import Error

# Database connection parameters
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "dispensary_management_system"

def create_connection():
    """Establishes and returns a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        if connection.is_connected():
            print('Connected successfully')
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return connection

create_connection()