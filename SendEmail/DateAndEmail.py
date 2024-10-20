import smtplib
import datetime as dt
import random
import  csv
import pandas

MY_EMAIL = "aliqulovdavron11@gmail.com"
MY_PASSWORD ="swkg tzqe rwom phbm" #"aogx ncrn cpzh jngd"

now=dt.datetime.now()
weekday=now.weekday()
if weekday==weekday:#Week day put
    with open("quotes.txt") as quote_text:
        all_quotes=quote_text.readlines()
        quote=random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="aliqulovdavron199@gmail.com",#MY_EMAIL,
            msg=f"Subject: Monday Motivational Quote\n\n{quote}"
        )
# with open("birthdays.csv","w") as data:
# bir={"name":["Mom","Dad"],"email":["aliqulovdavron199@gmail.com","aliqulovdavron760@gmail.com"],"year":[1974,1974],"month":[9,2],"day":[12,2]}
# data=pandas.DataFrame(bir)
# data.to_csv("birthdays.csv",index=False)
# print(data)


# my_email="aliqulovdavron@yahoo.com"
# password="aliqulovdavron@yahoo.com"
#
# connection=smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email ,password=password)
# connection.sendmail(from_addr=my_email ,to_addrs="aliqulovdavron11@gmail.com",msg="Hello")
# connection.close()

# import datetime as dt
#
# now=dt.datetime.now()
# # print(now)
# year=now.year
# month=now.month
# day=now.day
# hour=now.hour
# minute=now.minute
# second=now.second
# microsecond=now.microsecond
# day_of_week=now.weekday()
# day_of_birthday=dt.datetime(year=2001,month=3,day=9,hour=5)
# print(year,month,day,hour,minute,second,microsecond,day_of_week)
# print(day_of_birthday)