import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""select * from users;""")
users = cursor.fetchall()

print(users)