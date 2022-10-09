import pandas
import datetime as dt
import random
import smtplib

today = dt.datetime.today()
day = today.day
month = today.month
my_email = "@live.com"
my_password = " "
letters = []

data = pandas.read_csv("Day 32/birthdays.csv")
dates = data.to_dict()
birth_day = dates["day"][0]
birth_month = dates["month"][0]

for i in range(1,4):
    with open(f"Day 32/letter_templates/letter_{i}.txt") as file:
        letters.append(file.read())


if month == birth_month:
    if day == birth_day:
        name = dates["name"][0]
        friend_email = dates["email"][0]
        letter = random.choice(letters)
        b_letter = letter.replace("[NAME]", name)
        
        with smtplib.SMTP("smtp.office365.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=friend_email, 
                msg=f"Subject:HAPPY BIRTHDAY!\n\n{b_letter}"
            )







