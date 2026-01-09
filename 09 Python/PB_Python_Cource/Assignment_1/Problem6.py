#Q.Write a program to swap values of two numberes entered by the the user.

n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))

temp = n1
n1 = n2
n2 = temp

print("1st & 2nd numbers are swaped : ", n1, n2)

# Enter the 1st number : 1
# Enter the 2nd number : 2
# 1st & 2nd numbers are swaped :  2 1