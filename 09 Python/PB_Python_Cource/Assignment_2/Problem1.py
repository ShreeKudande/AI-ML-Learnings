#Q.Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
#if salary < 30,000 --> 5%
#if salary is 30,000 - 70,000 --> 15%
#if salary > 70,000 --> 25%

salary = int(input("Enter your salary please :" ))

if salary <= 30000:
    print("You Come under 5% tax bracket.")
elif salary > 30000 or salary < 70000:
    print("You Come under 15% tax bracket.")
elif salary > 70000:
    print("You Come under 15% tax bracket.")
else:
    print("Something went wrong, Please try again")

