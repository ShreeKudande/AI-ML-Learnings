"""
Q.Create a dictionary where:
Keys = student names
Values = marks (integer)
Write a menu-based program where user presses a key ('A','B','C','D') depending on the operation they want to perfrom on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks
"""
marks_data = {
    "Shree": 99,
    "Vivak": 75
}

user = input("Enter your choice (A/B/C/D): ").upper()

if user == "A":
    name = input("Enter new student name: ")
    marks = int(input("Enter marks: "))
    marks_data[name] = marks
    print("Student added.")

elif user == "B":
    name = input("Enter the student name to update marks: ")
    if name in marks_data:
        marks = int(input("Enter new marks: "))
        marks_data[name] = marks
        print("Marks updated.")
    else:
        print("Student not found.")

elif user == "C":
    name = input("Enter the student name to search: ")
    print(marks_data.get(name, "Student not found"))

elif user == "D":
    for name, marks in marks_data.items():
        print(name, marks)

else:
    print("Invalid choice.")

