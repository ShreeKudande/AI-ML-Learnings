#We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.
# Snake beats Water (drinks it),
# Water beats Gun (drowns it),
# Gun beats Snake (shoots it)
'''
import random

print("Game started!")

# Generate a random integer between 0 and 2 (inclusive)
comp = random.randint(0, 2)

user = input("Select any one [Snake, Water, Gun] : ")

if comp == 0:
    print("Computer choose : Snake")
    comp = "Snake"
elif comp == 1:
    print("Computer choose : Water")
    comp = "Water"
elif comp == 2:
    print("Computer choose : Gun")
    comp = "Gun"

if user == comp:
    print("Draw!")
elif user == "Snake" and comp == "Water":
    print("You Won!")
elif user == "Water" and comp == "Snake":
    print("You Lose!")
elif user == "Snake" and comp == "Gun":
    print("You Lose!")
elif user == "Gun" and comp == "Snake":
    print("You Won!")
elif user == "Water" and comp == "Gun":
    print("You Won!")
elif user == "Gun" and comp == "Water":
    print("You Lose!")
else:
    print("Something went wrong!")
'''

#More Correct Logical code -->
import random

print("Game started!")

# 1. Define the options in a list
options = ["Snake", "Water", "Gun"]

# 2. Computer selects directly from the list
comp = random.choice(options)

# 3. Take input and capitalize it immediately to prevent errors
user = input("Select any one [Snake, Water, Gun] : ").capitalize()

# Print computer choice
print(f"Computer choose: {comp}")


# 4. Logic Implementation
if user not in options:
    print("Invalid input! Please check your spelling.")
elif user == comp:
    print("Draw!")
elif (user == "Snake" and comp == "Water") or \
     (user == "Water" and comp == "Gun") or \
     (user == "Gun" and comp == "Snake"):
    print("You Won!")
else:
    print("You Lose!")
    