import yagmail
import json

with open("classified.json", "r") as file:
    data = json.load(file)

email = data.get("email")
password = data.get("password")

def send_email_to(reciever,message):
    yag = yagmail.SMTP(user=email, password=password)
    yag.send(to=reciever, subject="Nakupny zoznam", contents=message)
