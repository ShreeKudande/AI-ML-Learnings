class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        # print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language

# shree = Employee()
# shree.name = "Shree"
# print(shree.name, shree.language, shree.salary)

# rohan = Employee()

shree = Employee("Shri", 1300000, "javascript")
print(shree.name, shree.salary, shree.language)