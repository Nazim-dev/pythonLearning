numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [num * num for num in numbers]

# print(squared_numbers)

# result = [num for num in numbers if num % 2 == 0]

with open("Day 26/file1.txt") as file1:
    numbers1 = [int(num) for num in file1]

with open("Day 26/file2.txt") as file2:
    numbers2 = [int(num) for num in file2]


result = [num1 for num1 in numbers1 if num1 in numbers2 ]
print(result)