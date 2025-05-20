import pandas as pd
import smtplib
import datetime as dt
from email.message import EmailMessage

MY_EMAIL = 'demodemouser1002@gmail.com'
MY_PASSWORD = 'ypwbpoabvqtnxuue'

present = dt.datetime.now()
year = present.year
month = present.month
day = present.day

# reading csv file data
with open("birthdays.csv") as birthdays_file:
    birthdays = pd.read_csv(birthdays_file)
    df = pd.DataFrame(birthdays)
    records = df.to_dict(orient='records')
    users = {f"user{i+1}": record for i,record in enumerate(records)}


                # users = {'user1': {'name': 'Mother', 'email': 'demodemouser1002@gmail.com', 'year': 1980, 'month': 4, 'day': 23},
                #          'user2': {'name': 'Father', 'email': 'demodemouser1002@gmail.com', 'year': 1975, 'month': 1, 'day': 1},
                #          'user3': {'name': 'krishna', 'email': 'demodemouser1002@gmail.com', 'year': 2025, 'month': 5, 'day': 19}}

# opening and reading letter
with open("./letter_templates/letter_2.txt") as letter:
    letter_body = letter.read()

for user in users.items():
    #print(user)
    #user = ('user1', {'name': 'Mother', 'email': 'demodemouser1002@gmail.com', 'year': 1980, 'month': 4, 'day': 23})

    u_month = user[1]['month']
    u_day = user[1]['day']
    u_name = user[1]['name']
    u_email = user[1]['email']

    if u_month == month and u_day == day:
        msg = EmailMessage()
        msg['Subject'] = f"Happy Birthday {u_name}"
        msg["from"] = 'demodemouser1002@gmail.com'
        msg["To"] = u_email
        content = str(letter_body).replace('[NAME]',u_name)
        msg.set_content(content)

        #sending mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=MY_EMAIL,password= MY_PASSWORD)
             connection.send_message(msg)
