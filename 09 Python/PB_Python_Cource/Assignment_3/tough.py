#Q.Given a list of tuples with info(name, subject):

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

#a.List all unique course
# unique_course = set()

# for key, value in info:
#     unique_course.add(value)

# print(unique_course)

# OutPut :- {'Math', 'English', 'Science'}

#b.List students enrolled in English
# stu_enrolled_in_eng = set()

# for key, value in info:
#     if value == "English":
#         print(key)

#Output :- Alice, Charlie

#c.Create dictionary (student, set of courses)

dict = {}

for name, course in info:
    if (dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)

#Output :- 
# {
# 'Alice': {'Science', 'Math', 'English'}, 
# 'Bob': {'Science', 'Math'}, 
# 'Charlie': {'Math', 'English'}
# }
