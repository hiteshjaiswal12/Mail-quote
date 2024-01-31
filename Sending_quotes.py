import random
import smtplib
import datetime as dt
MY_EMAIL = "sunriserscap@gmail.com"
MY_PASSWORD = "odkybhvwgrycymjk"

now = dt.datetime.now()
weekday = now.weekday()
#print(weekday)
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()#Make a list of every line of quotes in file.
        quote = random.choice(all_quotes)

    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="hiteshpydeveloper@gmail.com",
                        msg=f"Subject:Monday MOtivation\n\n{quote}")
    connection.close()
