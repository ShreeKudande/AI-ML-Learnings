#Q. Write a function to return the count_digits the number of digits in a number, n.

def count_digits(n):
    counter = 0
    for i in n:
        if i == '-':
            continue
        counter+=1
    return counter

user = input("Enter the number : ")
print(count_digits(user))



