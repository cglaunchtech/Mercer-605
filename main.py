from flask import Flask, render_template, request
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


if __name__ == '__main__':
    app.run()