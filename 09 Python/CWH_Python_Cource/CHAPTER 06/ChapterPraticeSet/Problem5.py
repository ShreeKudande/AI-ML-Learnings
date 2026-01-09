#Q.Write a program which finds out whether a given name is present in a list or not. 

ls = ["shree", "saurabh", "vivak", "musthak", "shri"]

user = input("Enter any name to find in list : ")

if user in ls:
    print("Found!")
else:
    print("Not found!")


