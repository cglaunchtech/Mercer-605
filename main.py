from flask import Flask, render_template, request
from db.db import execute_query

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_query', methods=['POST'])
def execute_query_route():
    query = request.form['query']
    result = execute_query(query)
    return render_template('query_result.html', result=result)

if __name__ == '__main__':
    app.run()