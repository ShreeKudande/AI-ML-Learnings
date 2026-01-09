#Write a program to print multiplication table of a given number using for loop.

table = int(input("Enter the number : "))

for i in range(1, 11):
    print(f"{table} X {i} = {table*i}")
