from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ✅ Corrected keyword mappings
category_keywords = {
    "Mobile": ["phones", "phone", "mobiles", "smartphones"],
    "Laptop": ["laptops", "notebook"],
    "Headphones": ["headphones", "earphones", "earbuds"],
    "Smartwatch": ["watch", "watches", "smartwatches"]
}

def detect_category(query):
    query = query.lower()
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if f" {keyword} " in f" {query} ":  # Prevent matching "phone" in "headphones"
                return category
    return None

def search_products(query=""):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    matched_category = detect_category(query)

    if matched_category:
        cursor.execute('''
            SELECT DISTINCT * FROM products 
            WHERE LOWER(category) = ?
        ''', (matched_category.lower(),))
    elif query:
        cursor.execute('''
            SELECT DISTINCT * FROM products 
            WHERE LOWER(name) LIKE ? OR LOWER(brand) LIKE ? OR LOWER(category) LIKE ?
        ''', (f'%{query.lower()}%', f'%{query.lower()}%', f'%{query.lower()}%'))
    else:
        cursor.execute('SELECT DISTINCT * FROM products')

    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "brand": row[3],
            "price": row[4],
            "rating": row[5],
            "image_url": row[6],
            "availability": row[7]
        }
        products.append(product)

    return products

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(search_products())

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing "message" field'}), 400

    keyword = data['message']
    results = search_products(keyword)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)