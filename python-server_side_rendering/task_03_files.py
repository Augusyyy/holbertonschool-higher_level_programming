from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in products]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get('items', []))

@app.route('/products')
def products():
    source = request.args.get('source')
    products_data = []

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products_data = json.load(f)
        except Exception as e:
            print(f"Error loading JSON: {e}")  # 添加调试信息
            return render_template('product_display.html', error="Wrong source")
    elif source == 'csv':
        try:
            csv_file_path = '/Users/august/Desktop/pythonProject-ssr/products.csv'
            with open(csv_file_path, 'r') as f:
                reader = csv.DictReader(f)
                products_data = [row for row in reader]
        except Exception as e:
            print(f"Error loading CSV: {e}")  # 添加调试信息
            return render_template('product_display.html', error="Wrong source")
    elif source == 'db':
        try:
            db_path = 'products.db'
            products_data = read_sqlite(db_path)
        except Exception as e:
            print(f"Error loading database: {e}")  # 添加调试信息
            return render_template('product_display.html', error="Wrong source")
    else:
        return render_template('product_display.html', error="Wrong source")

    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)