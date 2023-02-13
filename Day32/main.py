import smtplib
import datetime as dt
import random

my_email = "ademircismtp@gmail.com"
password = "fcppakgcwytsotbt"


def read_data():
    with open("Day32/quotes.txt") as my_file:
        all_quotes = my_file.readlines()
        return random.choice(all_quotes)


def send_motivation_mail():

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="demirciworks@gmail.com",
            msg=f"Subject:Weekly motivation\n\n {read_data()} ")


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()  # get day number

date_of_birth = dt.datetime(year=1988, month=1, day=11)

if day_of_week == 0:
    send_motivation_mail()
