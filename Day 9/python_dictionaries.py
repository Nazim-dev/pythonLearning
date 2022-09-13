programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    }
#Retrieving items from dictionary
print(programming_dictionary["Bug"])

#adding new items to dictionary.

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a Dictionary in a dictionary

travel_logD = {
    "France": {"cities_visited": ["Paris", "Lille", "Marsielle"], "total_visits": 5},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"]}, "total_visits": 5
}

#Nesting dictionary in a list

travel_logL = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Marsielle"]
     , "total_visits": 5},

    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
      "total_visits": 5}
]