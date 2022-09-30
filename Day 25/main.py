# with open("Day 25/weather-data.csv") as file:
#     data = file.readlines()

# import csv

# with open("Day 25/weather-data.csv") as file:
#     data = csv.reader(file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))

import pandas 

data = pandas.read_csv("Day 25/weather-data.csv")
print(data["day"])