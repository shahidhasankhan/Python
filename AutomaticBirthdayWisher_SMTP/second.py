import smtplib
import datetime as dt
import random

today = dt.datetime.now()
if today.weekday() == 5:
    with open("quotes.txt", mode="r") as file:
        quotes = [quotes for quotes in file]
    quote_of_the_day = random.choice(quotes)

    my_email = "abc@gmail.com"
    password = "abc12345"
    target_email = "xyz@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=f"Subject:Quote of the Day.\n\n{quote_of_the_day}"
        )
