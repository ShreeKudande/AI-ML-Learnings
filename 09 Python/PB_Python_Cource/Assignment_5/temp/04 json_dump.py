import json

data = {
    "name": "Shree",
    "age": 20,
    "isTeacher": False
}

with open(r"D:\Python\PB_Python_Cource\Assignment_5\04 data.json", "w") as f:

    json.dump(data, f, indent = 4)
