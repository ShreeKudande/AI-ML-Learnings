#Q.Write a program to find whether a given username contains less than 10 characters or not.

user = input("Enter your name : ")

if len(user) < 10:
    print(f"You have less then 10 characters in your name...")
else:
    print(f"You have greater then 10 characters in your name...")

    