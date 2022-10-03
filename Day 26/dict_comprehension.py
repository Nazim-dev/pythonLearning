names = ['Dave', "Jack", "Manny", "Annie", "Vanessa"]

import random

student_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split()
result = {word:len(word) for word in words}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}


print(weather_f)