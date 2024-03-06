import sqlite3

def execute_query(query):
    conn = sqlite3.connect('db/sqlite_db')  # Change 'your_database.db' to your actual database file
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows