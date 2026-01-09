marks = {
    "Shree" : 100,
    "Rohan" : 56,
    "Vivak" : 80,
    0 : "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry" : 0})
del marks[0]
print(marks)

print(marks.get("Shri")) # Returns None
print(marks["Shri"]) # Returns Error

