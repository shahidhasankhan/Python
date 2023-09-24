import datetime as dt
import pandas
import random
import smtplib

PLACE_HOLDER = "[NAME]"
NUMBER_OF_TEMPLATES = 3

MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "123456"

today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_data_df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in birthdays_data_df.iterrows()}
birthdays_data_list = birthdays_data_df.to_dict(orient="records")
birthdays_today = []

# print(birthdays_dict)
#
# if today in birthdays_dict:
#     with open(f"./letter_templates/letter_{random.randint(1, NUMBER_OF_TEMPLATES)}.txt", mode="r") as letter:
#         birthday_person = birthdays_dict[today]
#         birthday_letter = letter.read()
#         birthday_letter = birthday_letter.replace(PLACE_HOLDER, birthday_person["name"])
#     print(birthday_letter)

for row in birthdays_data_list:
    if (row["month"], row["day"]) == today:
        birthdays_today.append(row)

for row in birthdays_today:
    letter_no = random.randint(1, NUMBER_OF_TEMPLATES)
    with open(f"./letter_templates/letter_{letter_no}.txt", mode="r") as letter:
        birthday_letter = letter.read()
        birthday_letter = birthday_letter.replace(PLACE_HOLDER, row["name"])

    print(birthday_letter)

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=row["email"],
    #         msg=f"Subject:Happy Birthday {row['name']}\n\n{birthday_letter_custom}"
    #     )
