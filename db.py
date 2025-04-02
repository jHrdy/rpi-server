import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""select * from cart;""")
rows = cursor.fetchall()
conn.commit()
conn.close()