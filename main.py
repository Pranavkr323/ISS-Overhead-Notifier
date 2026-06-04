import requests
from datetime import datetime, UTC
import smtplib as smtp
import time
import os

MY_LAT = 22.676908
MY_LNG = 88.383886
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def is_near():
      response = requests.get(url="http://api.open-notify.org/iss-now.json")
      response.raise_for_status()
      data = response.json()

      iss_latitude = float(data["iss_position"]["latitude"])
      iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

      return(MY_LAT-5 < iss_latitude < 5+MY_LAT
      and 
      MY_LNG-5 < iss_longitude < 5 + MY_LNG)

def is_dark():

      parameters = {
      "lat": MY_LAT,
      "lng": MY_LNG,
      "formatted": 0,
      }

      response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
      response.raise_for_status()
      data = response.json()
      sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
      sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

      time_now = datetime.now(UTC).hour

      return(time_now >= sunset or time_now <= sunrise)

while True:
      time.sleep(60)
      if is_near() and is_dark():
            with smtp.SMTP("smtp.gmail.com", port= 587) as connection:
                  connection.starttls()
                  connection.login(user=EMAIL, password= PASSWORD)
                  connection.sendmail( from_addr=EMAIL, to_addrs=TO_EMAIL,
                                        msg=f"Subject: ISS above you!\n\nThe ISS is near your location go outside to see!" )

