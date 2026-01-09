#Q. Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# 1. Get the two integers and one float from the user
# We use int() and float() to convert the string from input()
try:
    num1_int = int(input("Enter the first integer: "))
    num2_int = int(input("Enter the second integer: "))
    num3_float = float(input("Enter one float: "))

    # 2. Convert all to floats
    # We explicitly cast the integers to floats
    num1_float = float(num1_int)
    num2_float = float(num2_int)
    
    # num3_float is already a float

    # 3. Calculate the average
    average = (num1_float + num2_float + num3_float) / 3

    # 4. Print the result
    print(f"\nThe numbers are {num1_float}, {num2_float}, and {num3_float}.")
    print(f"Their average is: {average}")

except ValueError:
    print("\nError: You did not enter the correct data types.")
    print("Please make sure you enter two whole numbers and one number (which can have a decimal).")


# Enter the first integer: 10
# Enter the second integer: 10
# Enter one float: 10.5

# The numbers are 10.0, 10.0, and 10.5.
# Their average is: 10.166666666666666