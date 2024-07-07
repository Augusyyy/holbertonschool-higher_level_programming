import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


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


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

#
# @app.route('/products')
# def products():
#     source = request.args.get('source')
#     product_id = request.args.get('id')
#     products = []
#
#     if source == 'json':
#         products = read_json('products.json')
#     elif source == 'csv':
#         products = read_csv('products.csv')
#     else:
#         return render_template('product_display.html', error="Wrong source")
#
#     if product_id:
#         products = [product for product in products if product['id'] == int(product_id)]
#         if not products:
#             return render_template('product_display.html', error="Product not found")
#
#     return render_template('product_display.html', products=products)


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in products]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sqlite('products.db')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if product['id'] == int(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)