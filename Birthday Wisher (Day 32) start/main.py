import random
import smtplib
import datetime as dt

my_email = "davidmoshe110@gmail.com"
my_password = "*****************"

now = dt.datetime.now()
weekday = now.weekday()
weekday_name = now.strftime("%A") 
if weekday == 3:
    with open("E:/birthday-wisher/Birthday Wisher (Day 32) start/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
     connection.login(user=my_email, password=my_password)
     connection.sendmail(
        from_addr=my_email, to_addrs="davidlarmar349@yahoo.com", 
        msg=f"Subject:{weekday_name} Motivation\n\n {quote}"

        )



























# import smtplib

# my_email = "davidmoshe110@gmail.com"
# my_password = "rgyugohnqbwteiwf"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="davidlarmar349@yahoo.com", msg="Subject:just hello\n\n Hello from this side")































