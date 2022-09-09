#Take list of heights and find the average

student_heights = input("Input a list of student heights. ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
list_length = 0

for heights in student_heights:
    total += student_heights[list_length]
    list_length += 1


average = round(total / list_length)

print(f"The average height is {average}")