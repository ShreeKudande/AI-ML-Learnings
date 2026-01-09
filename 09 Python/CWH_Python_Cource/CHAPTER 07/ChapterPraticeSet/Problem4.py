#Write a program to find whether a given number is prime or not. 

user = int(input("Enter the number : "))

for i in range(2, user):
    if(user % i) == 0:
        print("Number is not Prime")
        break
else:  
    print("Number is Prime")
