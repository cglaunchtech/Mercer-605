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

def select_past_orders(customer_id):
    conn = sqlite3.connect('db/bike_store_db')
    cursor = conn.cursor()
    customer_id = 1445
    query = '''
        SELECT order_id, order_status, order_date, required_date, shipped_date,
               product_id, product_name, model_year, product_list_price,
               brand_name, category_name
        FROM order_details
        WHERE customer_id = ?
    '''
    cursor.execute(query, (customer_id,))
    rows = cursor.fetchall()

    # Print the fetched rows
    for row in rows:
        print(row)

    # Close the connection
    conn.close()
    params = (customer_id,)
    past_orders = fetch_query(query, params)
    return past_orders