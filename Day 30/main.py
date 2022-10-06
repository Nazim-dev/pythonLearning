#FileNotFound

try:
    file = open("Day 30/body.txt")
    the_dict = {"key": "value"}
    print(the_dict["newkey"])
except FileNotFoundError:
    file = open("Day 30/body.txt", "w")
    file.write("file created")
except KeyError as error:
    print(f"The key {error} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)