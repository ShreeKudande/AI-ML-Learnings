#Q.Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def greet():
        print("hello")

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square root is {self.n**(1/2)}")

a = Calculator(4)
a.square()
a.cube()
a.square_root()

a.greet()

b = Calculator(25)
b.square()
b.cube()
b.square_root()
