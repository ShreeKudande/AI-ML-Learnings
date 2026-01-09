'''
Docstring for CWH_Python_Cource.CHAPTER 08.05_recursion
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n  x n-1 x .....x 1
factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if n == 1 or n == 0: #it resolves the recursion from running infinitely
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number : "))

print(f"The factorial of this number is {factorial(n)}")

