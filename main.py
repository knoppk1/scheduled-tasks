# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
SMTP = os.environ.get("MY_SMTP")

PATH = "birthdays.csv"
PORT = 587

now = dt.datetime.now()
day = now.day
month = now.month
df = pandas.read_csv(PATH)
birthdays = df[(df["month"] == month) & (df["day"] == day)]
if not birthdays.empty:
    for (index,row) in birthdays.iterrows():

        name = row["name"]
        email = row["email"]

        with open(f"letter_templates/letter_{randint(1,3)}.txt") as file:
            text = file.read().replace("[NAME]",name)

        with smtplib.SMTP(host=SMTP,port=PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday\n\n{text}")
