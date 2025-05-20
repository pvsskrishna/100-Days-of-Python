from calendar import month
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = 'demodemouser1002@gmail.com'
MY_PASSWORD = 'ypwbpoabvqtnxuue'

today = datetime.now()
today_tuple = (today.month , today.day)

data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

#dictionary_comprehension = {new_key:new_value for (key,value) in dict.items()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    birthday_person_name = birthday_person["name"]

    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        message = f"Subject:Happy Birthday {birthday_person_name}! \n\n{contents}"
        connection.sendmail(
            to_addrs=birthday_person['email'],
            from_addr=MY_EMAIL,
            msg= message
        )