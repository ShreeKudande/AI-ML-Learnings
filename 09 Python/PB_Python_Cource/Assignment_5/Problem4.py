#Q.Create a Python dictionary of 3 cities and their populations. Save it to "citites.json".
# 1.Then load the JSON and print each city and its population.
# 2.Ask the user for a new city & its population -update this info in the json file.

import json

my_dict = {
    "Pune": "75 lakhs",
    "Mumbai": "2.21 crore",
    "Delhi": "3.47 crore"
}

file_path = r"D:\Python\PB_Python_Cource\Assignment_5\citites.json"

with open(file_path, "w") as f:
        json.dump(my_dict, f, indent=4)


with open(file_path, "r") as f:
        data = json.load(f)
        print(data)

new_city = input("Enter the city name : ")
new_city_population = input("Enter the city population : ")
add_city = {new_city: new_city_population}
my_dict.update(add_city)

file_path = r"D:\Python\PB_Python_Cource\Assignment_5\citites.json"

with open(file_path, "w") as f:
        json.dump(my_dict, f, indent=4)

