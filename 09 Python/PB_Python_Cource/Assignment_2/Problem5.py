#Q.Write a function to return the sum of digits of a number, n.

def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total+= n % 10
        n //= 10
    return total

user = int(input("Enter the number : "))
print(sum_of_digits(user))
