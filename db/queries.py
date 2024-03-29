from db.db import execute_query, fetch_query


def select_customers():
    query = 'SELECT * FROM customers ORDER BY customer_id DESC LIMIT 10'
    customers = fetch_query(query)
    return customers


def search_customers(query):
    search_query = '%' + query + '%'
    query = '''SELECT * FROM customers 
               WHERE first_name LIKE ? OR last_name LIKE ? OR phone LIKE ? OR email LIKE ? 
               OR street LIKE ? OR city LIKE ? OR state LIKE ? OR zip_code LIKE ?'''
    params = (
        search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query)
    customers = fetch_query(query, params)
    return customers


def insert_customer(first_name, last_name, phone, email, street, city, state, zipcode):
    query = 'INSERT INTO customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (?, ?, ' \
            '?, ?, ?, ?, ?, ?) '
    execute_query(query, (first_name, last_name, phone, email, street, city, state, zipcode))


def update_customer(first_name, last_name, phone, email, street, city, state, zipcode):
    query = 'UPDATE customers SET first_name = ?, last_name = ?, phone = ?, email = ?, street = ?, city = ?, ' \
            'state = ?, zip_code = ? WHERE customer_id = ? '
    execute_query(query, (first_name, last_name, phone, email, street, city, state, zipcode))
