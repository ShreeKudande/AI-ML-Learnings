class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

shree = Employee()
shree.language = "JavaScript"
print(shree.salary, shree.language)

shree.getInfo()
Employee.getInfo(shree)

shree.greet()