##################### Extra Hard Starting Project ######################
import os
import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")         

dict = data.to_dict(orient="records") 

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

for item in dict:
    if item["month"] == month and item["day"]==day:
        print("Trovata una corrispondenza")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        num = random.randint(1,3)
        print(num)
        with open(f"letter_templates/letter_{num}.txt", "r") as letter:
            content = letter.read()
            print("-------------------------------------")
            print(content)
            print("-------------------------------------")
            name = item["name"]
            new_content = content.replace("[NAME]",name)
            print("-------------------------------------")
            print(new_content)



        
# 4. Send the letter generated in step 3 to that person's email address.                
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()       
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL,
                msg=f"Subject:Happy Birthday Now!'\n\n{new_content}"               
                )




