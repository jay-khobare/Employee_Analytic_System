import mysql.connector

def get_db_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="er@jay01",
        database="employee_analytics"
    )
    return connection

print("Connection Successfully Establish!!!!!")