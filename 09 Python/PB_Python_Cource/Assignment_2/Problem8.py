#Q.Let's create a simple calculator that performs arithmetic operations. Create a function calculator(a,b,operation) that performs additon, subtraction, multiplication, or division based on the operation parameter.
# Operation parameter can have values '+', '-', '*' & '/'.

def calculator(a, b, operation):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "%":
            if b == 0:
                return "Undefined "
            return a % b
        case "/":
            if b == 0:
                return "Undefined "
            return a / b
        case _:
            return "Invalid operation"

n1 = int(input("Enter N1 : "))
n2 = int(input("Enter N2 : "))
operation = input("Operation : ")

print(calculator(n1, n2, operation))

