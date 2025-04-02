import yagmail
import json

with open("classified.json", "r") as file:
    data = json.load(file)

email = data.get("email")
password = data.get("pass")

def send_email_to(reciever,message):
    print('sending mail')
    yag = yagmail.SMTP(user=email, password=password)
    yag.send(to=reciever, subject="Nakupny zoznam", contents=message)