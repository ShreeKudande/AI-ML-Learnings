#Q.Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

p = int(input("Enter physics marks : "))
c = int(input("Enter chemistry marks : "))
m = int(input("Enter math marks : "))

percentile = ((p+c+m)/300)*100
print(f"Percentile : {percentile}%")

if percentile > 40 and p > 33 and c > 33 and m > 33:
    print("Pass")
else:
    print("Fail")

