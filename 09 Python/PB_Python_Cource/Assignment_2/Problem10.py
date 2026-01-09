#Q.Let's create a "Number Guessing Game". Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
#"Too high" if the guess is above the number
#"Too low" if the guess is below
#"Correct!" if the guess matches

n = 22
user = 0

while n != user:
    user = int(input("Enter the number : "))
    if n > user:
        print("Too low")
    elif n < user:
        print("Too high")

print("Correct!")

