import sqlite3

def execute_query(query, params=None):
    conn = sqlite3.connect('db/bike_store_db')
    cursor = conn.cursor()
    if params:
        print("Executing query with params:", query, params)  # Debugging statement
        cursor.execute(query, params)
    else:
        print("Executing query:", query)  # Debugging statement
        cursor.execute(query)
    conn.commit()
    conn.close()


def fetch_query(query, params=None):
    conn = sqlite3.connect('db/bike_store_db')
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
        print("Executing query with params:", query, params)  # Debugging statement
    else:
        print("Executing query:", query)  # Debugging statement
        cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows