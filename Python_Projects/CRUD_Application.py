import psycopg2
from tabulate import tabulate

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",       # your database name
    user="postgres",     # your PostgreSQL username
    password="root",     # your PostgreSQL password
    host="localhost",
    port="5432"
)

def insert():
    name = input("Enter Name : ")
    age = input("Enter Age : ")
    address = input("Enter Address : ")
    contact = input("Enter Contact : ")
    mail = input("Enter Mail : ")

    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO data (name, age, address, contact, mail) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, (name, age, address, contact, mail))
            conn.commit()
            print("\nRecord Inserted Successfully")
    except Exception as e:
        print(f"Error: {e}")

def select():
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM data")
            result = cur.fetchall()
            print("\n")
            print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS","CONTACT","MAIL"], tablefmt="fancy_grid"))
    except Exception as e:
        print(f"Error: {e}")

def update():
    fields = {1: "name", 2: "age", 3: "address", 4: "contact", 5: "mail"}
    print("1.Name\n2.Age\n3.Address\n4.Contact\n5.Mail")
    option = int(input("\nWhich field you want to update?: "))
    
    if option in fields:
        pid = input("Enter Your ID: ")
        value = input(f"Enter new {fields[option]}: ")
        try:
            with conn.cursor() as cur:
                sql = f"UPDATE data SET {fields[option]} = %s WHERE pid = %s"
                cur.execute(sql, (value, pid))
                conn.commit()
                print("\nUpdate Successfully")
                select()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid Option")

def delete():
    pid = input("Enter Your ID: ")
    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM data WHERE pid = %s"
            cur.execute(sql, (pid,))
            conn.commit()
            print("\nRecord Deleted Successfully")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\n1.Insert Record\n2.Select Record\n3.Update Record\n4.Delete Record\n5.Exit\n")
    choice = int(input("Enter Your Choice : "))
    
    if choice == 1:
        insert()
    elif choice == 2:
        select()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        conn.close()
        print("Connection closed. Exiting...")
        break
    else:
        print("Invalid Option")
