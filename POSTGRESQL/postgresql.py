import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",   # your database name
    user="postgres",        # your username
    password="root",  # replace with your password
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Run a query
cur.execute("SELECT * FROM details;")

# Fetch results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()






print("\nNew Database Connection")
print("---------------------")
# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="Database2",   # your database name
    user="postgres",        # your username
    password="root",  # replace with your password
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Run a query
cur.execute("SELECT * FROM records;")

# Fetch results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
