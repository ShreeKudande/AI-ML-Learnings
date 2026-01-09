#Write a program to calculate the factorial of a given number using for loop. 

user = int(input("Enter the number : "))

ftr = 1
# for i in range(user, 1, -1):
#     ftr *= i
for i in range(1, user+1):
    ftr *= i

print(ftr)