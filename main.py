# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "tadaichilopez@gmail.com"
my_password = "ctsijmoqdvuyplpn"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    random_num = random.randint(1,3)
    with open(f"letter_templates/letter_{random_num}.txt") as letter:
        data = letter.read()
        data = data.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # email encryption
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!!!\n\n{data}"
        )
