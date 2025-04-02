from flask import Flask, render_template, request
import sqlite3
from send_email import send_email_to

app = Flask(__name__)

def format_db_output(data):
    txt = "Potrebujeme kupit "
    for key, val in data.items():
        txt += f'{val}x {key}\n'
    return txt


def get_users():
    '''conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""select name from users;""")
    users = cursor.fetchall()

    cursor.execute("""select email from users;""")
    mails = cursor.fetchall()'''
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""select * from users;""")
    users = cursor.fetchall()

    return users

def print_cart():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""select item from cart;""")  
    items = cursor.fetchall()
    
    cursor.execute("""select quantity from cart;""")
    quant = cursor.fetchall()
    
    data = {items[i][0]:quant[i][0] for i in range(len(quant))}

    return format_db_output(data) 

@app.route("/", methods=['GET', 'POST'])
def site():
    cart = None
    mail = None
    users = get_users()
    print(users)
    user_names = []
    emails = []
    cart = print_cart()

    for _, name, email in users:
        user_names.append(name)    
        emails.append(email)

    if request.method == 'POST' and request.form.get('getlist'):
        cart = print_cart()
        print(cart)
    
    if request.method == 'POST' and (id:=request.form.get('user_button')):
        send_email_to(emails[int(id)-1], cart)

    return render_template("index.html", cart=cart, users=users, mail=mail)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)