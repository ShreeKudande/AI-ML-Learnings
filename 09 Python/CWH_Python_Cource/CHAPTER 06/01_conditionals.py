user = int(input("Enter your age : "))

if(user > 100 or user < 1):
    print("You Entered invalid age!")
elif(user >= 18):
    print("You can drive!")
else:
    print("You can't drive!")

