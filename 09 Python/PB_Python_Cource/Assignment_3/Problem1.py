#Q.Ask the user for a string and check whether it is a palindrome or not. A palindrome is a string which is same when we read it forward & backward. Eg - "madam", "racecar" etc.

user = input("Enter the word : ")

if user == user[::-1]:
    print("It's Palindrome")
else:
    print("It's not a Palindrome")

