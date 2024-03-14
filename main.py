from flask import Flask, render_template, request, jsonify

from db.db import select_past_orders
from db.queries import select_customers, search_customers

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query', '')  # Get the search query from the form data
        customers = search_customers(query)  # Perform customer search
    else:
        customers = select_customers()  # Fetch all customers
    return render_template('index.html', customers=customers)

@app.route('/get_past_orders', methods=['GET'])
def get_past_orders():
    customer_id = request.args.get('customer_id')
    past_orders = select_past_orders(customer_id)
    print("Past orders:", past_orders)  # Add this line to print past_orders
    return jsonify(past_orders)

if __name__ == '__main__':
    app.run()