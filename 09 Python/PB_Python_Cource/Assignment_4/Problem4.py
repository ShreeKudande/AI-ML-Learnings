#Q.Create a class Student with private attributes _name, _roll_no, and _marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 & name cannot be empty).

class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # GETTERS
    def get_name(self):
        return self.__name
    
    def get_roll_no(self):
        return self.__roll_no
    
    def get_marks(self):
        return self.__marks

    # SETTERS with VALIDATION
    def set_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty")
        self.__name = name

    def set_roll_no(self, roll_no):
        if not (1 <= roll_no <= 100):
            raise ValueError("Roll number must be between 1 and 100")
        self.__roll_no = roll_no

    def set_marks(self, marks):
        if marks < 0:
            raise ValueError("Marks cannot be negative")
        self.__marks = marks

    # Print student
    def get_student(self):
        print(f"Student name: {self.__name}, Roll No: {self.__roll_no}, Marks: {self.__marks}")

    # Edit using setters
    def edit_student(self, new_name, new_roll_no, new_marks):
        self.set_name(new_name)
        self.set_roll_no(new_roll_no)
        self.set_marks(new_marks)


# TESTING
s1 = Student("Shree", 56, 100)
s2 = Student("Saurabh", 45, 82)

s1.get_student()
s2.get_student()

s1.edit_student("Saurabh", 45, 82)
s2.edit_student("Shree", 56, 100)

print()
s1.get_student()
s2.get_student()

s2.get_student()
