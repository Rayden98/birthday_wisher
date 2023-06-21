import smtplib
import datetime as dt
import random
import time
import pandas

# ----------------------CONSTANTS ---------------------------- #
my_email = "royalesanmiguelc@gmail.com"
password = "pddfdvtnqkkxfneg"
now = dt.datetime.now()
day_of_month = int(now.strftime("%d"))
month = now.month

# ----------------- OPENING THE MESSAGES ----------------------#
data = pandas.read_csv("birthdays.csv")
dictionary = data.to_dict(orient="records")
print(dictionary)
# ------------------ SENDING THE MESSAGE --------------------- #

# time.sleep(10)
for each in dictionary:
    time.sleep(3)
    if each["month"] == day_of_month and each["day"] == month:
        random_quote = random.choice(data)
        each_name = each["name"]
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="rember98cjs@gmail.com",
                msg=f"subject=Happy Birthday\n\nHey{each_name},\nHappy birthday! Have a wonderful time today and eat "
                    f"lots of cake!\n Losts of love\nEnmanuel")
            connection.close()
