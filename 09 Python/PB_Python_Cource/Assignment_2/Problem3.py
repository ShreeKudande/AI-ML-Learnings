#Write a function that prints the digits of a number, n.
# for eg: n = 312, there are 3 digits in it 3, 1 and 2 & we need to print them.
#[Hint - The right most digit of a number N is N % 10.
#And to remove that right most digit from a number, we can do N = N / 10.]

# def sep(n):
#     for i in n:
#         print(i)

# n = input("Enter the number : ")
# sep(n)

def sep(n):
    # Loop as long as the number is greater than 0
    while n > 0:
        # 1. Get the rightmost digit (Hint: N % 10)
        digit = n % 10
        # 2. Print the digit
        # Note: If we want to print them in the correct order (left-to-right), 
        # we'd need to store them in a list/stack and print them in reverse later.
        # For simplicity, if printing them reverse (right-to-left) is acceptable:
        print(digit)
        
        # 3. Remove the rightmost digit (Hint: N = N // 10)
        n = n // 10

# Get input and convert it to an integer
n_str = input("Enter the number: ")
n = int(n_str) 
sep(n)