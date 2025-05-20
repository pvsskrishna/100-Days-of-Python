import smtplib
import datetime as dt
import random
from email.message import EmailMessage

my_gmail = "demodemouser1002@gmail.com"
password = "ypwbpoabvqtnxuue"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote_of_the_day = str(random.choice(all_quotes))

    print(quote_of_the_day)

    msg = EmailMessage()
    msg["Subject"] = "Friday Motivation"
    msg["from"] = my_gmail
    msg["To"] = "varuntesting@myyahoo.com"
    msg.set_content(quote_of_the_day)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.send_message(msg)



"""#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
"""