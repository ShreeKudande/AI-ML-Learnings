#Q.Write a program using functions to find greatest of three numbers.

def greatest_num(a, b, c):
    if a > b and a > c:
        print(f"Greatest number is {a}")
    elif b > a and b > c:
        print(f"Greatest number is {b}")
    else:
        print(f"Greatest number is {c}")

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

greatest_num(a, b, c)
