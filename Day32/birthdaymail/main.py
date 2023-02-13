import smtplib
import datetime as dt
import random
import pandas as pd

now = dt.datetime.now()
today = (now.month, now.day)

my_email = "ademircismtp@gmail.com"
password = "fcppakgcwytsotbt"

data = pd.read_csv("Day32/birthdaymail/birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"])
                   : data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"Day32/birthdaymail/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents= contents.replace("[NAME]", birthday_person["name"])
        print(contents)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n {contents} ")
