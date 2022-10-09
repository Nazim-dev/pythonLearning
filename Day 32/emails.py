import smtplib
import datetime as dt
import random
now = dt.datetime.now()
day = now.weekday()

with open("Day 32/quotes.txt") as file:
    for item in file:      
        quotes = file.readlines()
    
    today_quote = random.choice(quotes)

if day == 5:
    print("true")
    my_email = "@live.com"
    my_password = " "

    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="@gmail.com", 
            msg=f"Subject:Motivation\n\n{today_quote}"
        )

