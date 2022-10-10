import requests


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()


# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]

# position = (longitude, latitude)
# print(position)

parameters = {
    "lat": 12.169174,
    "lng": -61.726143,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)