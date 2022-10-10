import smtplib
import requests
from datetime import datetime

MY_LAT = 12.169174
MY_LONG = -61.726143 

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smpt.office365.com")
    connection.starttls()
    connection.login("myemail@outlook.com", "123556asd")
    connection.sendmail(
        from_addr="myemail@outlook.com",
        to_addrs="someone@gmail.com",
        msg="Subject:ISS\n\n The ISS is close, go look at the sky"
    )



