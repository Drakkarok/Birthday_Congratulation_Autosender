import pandas
import datetime
import smtplib
import random

email_dummy = "dummy@Gmail.com"
password = "password"
df = pandas.read_csv("birthdays.csv")
now = datetime.datetime.now()


if df[df["day"] == now.day] is not None and df[df["month"] == now.month] is not None:
    filtered_df = df.query("day == @now.day and month == @now.month")
    selected_df = filtered_df[["name", "year", "email"]]
    indexed_df = selected_df.set_index("name")
    birthday_dict = indexed_df.to_dict("index")
    for key, value in birthday_dict.items():
        random_number = random.choice(range(1, 4))
        with open(f"./letter_templates/letter_{random_number}.txt", "r") as file:
            content = file.read()
            modified_content = content.replace("[NAME]", key)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email_dummy, password)
            connection.sendmail(from_addr=email_dummy, to_addrs=(key, value['email']), msg=f"Subject:Happy birthday!"
                                                                                           f"\n\n{modified_content}")
