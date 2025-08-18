import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",      # change if needed
        user="postgres",        # your DB username
        password="root",
        host="localhost",
        port="5432"
    )
    print("✅ Connected to PostgreSQL!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
