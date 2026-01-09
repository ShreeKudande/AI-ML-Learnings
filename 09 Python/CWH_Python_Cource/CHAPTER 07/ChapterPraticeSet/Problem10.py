# Write a program to print multiplication table of n using for loops in reversed order.

user = int(input("Enter the number : "))

# for i in range(10, 0, -1):
#     print(f"{user} X {i} = {user*i}")

for i in range(1, 11):
    print(f"{user} X {11-i} = {user*(11-i)}")

    