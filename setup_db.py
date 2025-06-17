import sqlite3

def create_tables():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Product master table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT,
        sku TEXT,
        category TEXT,
        subcategory TEXT,
        name TEXT,
        description TEXT,
        tax REAL,
        price REAL,
        unit TEXT,
        image_path TEXT
    )
    """)

    # Goods Receiving table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods_receiving (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        supplier TEXT,
        quantity REAL,
        unit TEXT,
        rate REAL,
        total REAL,
        tax REAL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    """)

    # Sales table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        customer TEXT,
        quantity REAL,
        unit TEXT,
        rate REAL,
        total REAL,
        tax REAL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    """)

    # Insert 2 operator accounts
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin1", "admin123"))
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin2", "admin234"))

    conn.commit()
    conn.close()
    print("Database setup completed!")

if __name__ == "__main__":
    create_tables()
