# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close database connection

import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='pg' password='1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='database1' user='pg' password='1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity, price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='pg' password='1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    row=cur.fetchall()
    conn.close()
    return row

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='pg' password='1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price,item):
    conn=psycopg2.connect("dbname='database1' user='pg' password='1234' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price,item))
    conn.commit()
    conn.close()

create_table()
insert('Orange', 50, 5.55)
print(view())
update(11,6,"Orange")
print(view())
