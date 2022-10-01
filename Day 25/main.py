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

# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()


#Get Data in Columns

# print(data.condition)

#Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print((monday.temp * 1.8) + 32)

#Create a dataframe

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# student_data = pandas.DataFrame(data_dict)

# student_data.to_csv("student.csv")