import sqlite3

# Connect to SQLite database (creates it if not exists)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    brand TEXT,
    price REAL,
    rating REAL,
    image_url TEXT,
    availability TEXT
)
''')

# Optional: clear existing entries to avoid duplicates
cursor.execute('DELETE FROM products')

# Mock product data
products = [
    {"name": "Apple iPhone 14 Pro Max", "category": "Mobile", "brand": "Apple", "price": 139999, "rating": 4.9, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71yzJoE7WlL._SL1500_.jpg"},
    {"name": "Samsung Galaxy S23 Ultra", "category": "Mobile", "brand": "Samsung", "price": 124999, "rating": 4.8, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61RZDb2mQxL._SL1500_.jpg"},
    {"name": "OnePlus 11 5G", "category": "Mobile", "brand": "OnePlus", "price": 56999, "rating": 4.5, "availability": "Limited Stock", "image_url": "https://m.media-amazon.com/images/I/61TnX0PmqES._SL1500_.jpg"},
    {"name": "Xiaomi Redmi Note 12 Pro+", "category": "Mobile", "brand": "Xiaomi", "price": 29999, "rating": 4.3, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/81FeKFPtq-L._SL1500_.jpg"},
    {"name": "Realme Narzo 60 Pro", "category": "Mobile", "brand": "Realme", "price": 23999, "rating": 4.2, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71n7w5KJcBL._SL1500_.jpg"},
    {"name": "Google Pixel 7A", "category": "Mobile", "brand": "Google", "price": 43999, "rating": 4.4, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61BAu3fJ5-L._SL1500_.jpg"},
    {"name": "Samsung Galaxy Watch 6", "category": "Smartwatch", "brand": "Samsung", "price": 29999, "rating": 4.6, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71d93zrWW-L._SL1500_.jpg"},
    {"name": "Apple Watch Series 8", "category": "Smartwatch", "brand": "Apple", "price": 44999, "rating": 4.8, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71ybG9pEHjL._SL1500_.jpg"},
    {"name": "boAt Xtend Smartwatch", "category": "Smartwatch", "brand": "boAt", "price": 2499, "rating": 4.1, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61IMRs+o0iL._SL1500_.jpg"},
    {"name": "Noise ColorFit Pro 4", "category": "Smartwatch", "brand": "Noise", "price": 3499, "rating": 4.0, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61G9Z4F0P9L._SL1500_.jpg"},
    {"name": "Sony WH-1000XM5", "category": "Headphones", "brand": "Sony", "price": 29990, "rating": 4.7, "availability": "Limited Stock", "image_url": ""},
    {"name": "JBL Tune 760NC", "category": "Headphones", "brand": "JBL", "price": 5999, "rating": 4.4, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61NEXl2FfjL._SL1500_.jpg"},
    {"name": "boAt Rockerz 450", "category": "Headphones", "brand": "boAt", "price": 1499, "rating": 4.3, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61kWB+uzR2L._SL1500_.jpg"},
    {"name": "Apple AirPods Pro (2nd Gen)", "category": "Headphones", "brand": "Apple", "price": 24990, "rating": 4.8, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61f1YfTkTDL._SL1500_.jpg"},
    {"name": "HP Pavilion x360", "category": "Laptop", "brand": "HP", "price": 62999, "rating": 4.5, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71YVa6G0E3L._SL1500_.jpg"},
    {"name": "Dell Inspiron 15", "category": "Laptop", "brand": "Dell", "price": 57999, "rating": 4.2, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71hG+e7roXL._SL1500_.jpg"},
    {"name": "Lenovo Legion 5", "category": "Laptop", "brand": "Lenovo", "price": 89999, "rating": 4.6, "availability": "Limited Stock", "image_url": "https://m.media-amazon.com/images/I/61HTsRZCgVL._SL1500_.jpg"},
    {"name": "MacBook Air M2", "category": "Laptop", "brand": "Apple", "price": 114999, "rating": 4.9, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71TPda7cwUL._SL1500_.jpg"},
    {"name": "Asus ROG Zephyrus", "category": "Laptop", "brand": "Asus", "price": 139999, "rating": 4.7, "availability": "Limited Stock", "image_url": "https://m.media-amazon.com/images/I/71K7QkP3v9L._SL1500_.jpg"},
    {"name": "Mi Notebook Ultra", "category": "Laptop", "brand": "Xiaomi", "price": 59999, "rating": 4.4, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71zlb1vD5WL._SL1500_.jpg"},
    {"name": "iPad Air (5th Gen)", "category": "Tablet", "brand": "Apple", "price": 59900, "rating": 4.8, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61XZQXFQeVL._SL1500_.jpg"},
    {"name": "Samsung Galaxy Tab S8", "category": "Tablet", "brand": "Samsung", "price": 69999, "rating": 4.6, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/71UKaYl9WEL._SL1500_.jpg"},
    {"name": "Amazon Echo Dot (5th Gen)", "category": "Smart Speaker", "brand": "Amazon", "price": 4499, "rating": 4.4, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61dHtKcDt6L._SL1500_.jpg"},
    {"name": "Google Nest Mini", "category": "Smart Speaker", "brand": "Google", "price": 3499, "rating": 4.3, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/61DrdxMsyAL._SL1500_.jpg"},
    {"name": "Canon EOS 1500D DSLR", "category": "Camera", "brand": "Canon", "price": 45999, "rating": 4.5, "availability": "In Stock", "image_url": "https://m.media-amazon.com/images/I/914hFeTU2-L._SL1500_.jpg"}
]

# Insert into table
for product in products:
    cursor.execute('''
        INSERT INTO products (name, category, brand, price, rating, image_url, availability)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        product['name'],
        product['category'],
        product['brand'],
        product['price'],
        product['rating'],
        product['image_url'],
        product['availability']
    ))

# Save changes and close
conn.commit()
conn.close()

print("✅ Database populated with mock products.")