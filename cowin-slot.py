import smtplib
import requests
import datetime
import json
import time
from datetime import date
from urllib.request import Request,urlopen

today = date.today().strftime("%d-%m-%y")
count = 0

pincodes = ["784164","781017","784161","787001"]

date = 0
temp = str(14) + "-05-21"


while True:

    for i in range(0,8):
        temp = str(23+i) + "-05-21"
        for pincode in pincodes:
            req = Request(
                "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + temp,
                headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            data = json.loads(webpage)
            for center in data["centers"]:
                for session in center["sessions"]:
                    print("\t", center["name"])
                    print("\t", center["address"])
                    print("\t Price: ", center["fee_type"])
                    print("\t", session["vaccine"])
                    print("\t Age limit:", session["min_age_limit"])
                    print("\t Available Capacity: ", session["available_capacity"])
                    print("////////////////////////////////////////////////////")
                    if int(session["available_capacity"]) > 0:
                        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        server.login("noreplydeveloperteam12@gmail.com", "bijuborahkvcut")
                        if pincode == "784164":
                            server.sendmail("noreplydeveloperteam12@gmail.com", "bijuborah2017@gmail.com",
                                            "Vaccine available , Kindly check your cowin app")
                        elif pincode == "781017":
                            server.sendmail("noreplydeveloperteam12@gmail.com", "mushkangiri19@gmail.com",
                                            "Vaccine available , Kindly check your cowin app")
                            server.sendmail("noreplydeveloperteam12@gmail.com", "Vishnugiri2003@gmail.com",
                                            "Vaccine available , Kindly check your cowin app")
                        else:
                            server.sendmail("noreplydeveloperteam12@gmail.com", "bijuborah2017@gmail.com",
                                            "Vaccine available , Kindly check your cowin app")
                        server.quit()
        time.sleep(20)