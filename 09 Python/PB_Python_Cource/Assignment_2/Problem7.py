#Q.Design a program to continously input a number n from user & print if it is positive or negative until the user enters "Quit".


while True:
    n = input("Enter the Number : ")

    if n == "Quit":
        break
    try:
        if int(n) < 0:
            print("NEGATIVE")
        elif int(n) > 0:
            print("POSITIVE")
        else:
            print("ZERO")
        
    except ValueError:
        # If int(n) fails (e.g., user typed "hello"), Python jumps here
        print("Invalid input! Please enter a number.")

