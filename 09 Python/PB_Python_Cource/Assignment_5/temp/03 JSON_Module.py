#JavaScript Object Notation

import json

json_str = '{"name" : "Shree", "isTeacher" : false}'
print(type(json_str))
print(json_str)

py_obj = json.loads(json_str) #JSON to Python

print(type(py_obj))
print(py_obj)

json_str = json.dumps(py_obj) #Python to JSON
print(type(json_str))
print(json_str)

# <class 'str'>
# {"name" : "Shree", "isTeacher" : false}

# <class 'dict'>
# {'name': 'Shree', 'isTeacher': False}

# <class 'str'>
# {"name": "Shree", "isTeacher": false}

with open(r"D:\Python\PB_Python_Cource\Assignment_5\03 data.json", "r") as f:

    python_object = json.load(f)
    print(python_object)

# {'name': 'Shree', 'isTeacher': False, 'address': {'city': 'Pune', 'country': 'India'}, 'subjects': ['Python', 'AI/ML']}

