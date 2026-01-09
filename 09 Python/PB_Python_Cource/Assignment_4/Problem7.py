#Q.Create a class Person that allows the constructor to work with:
#name only
#name + age
#name + age + address
#As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.

class Person:
    def __init__(self, name = None, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}, Address : {self.address}")


p1 = Person("Shree")
p2 = Person("Shree", 20)
p3 = Person("Shree", 20, "India")

p1.display()
p2.display()
p3.display()

