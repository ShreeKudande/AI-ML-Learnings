#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

print("Game started!")

options = ["Snake", "Water", "Gun"]

com_score = 0
user_score = 0
i = 0
while(i < 3):

    comp = random.choice(options)
    user = input("Select any one [Snake, Water, Gun] : ").capitalize()
    print(f"Computer choose: {comp}")

    if user not in options:
        print("Invalid input! Please check your spelling.")
    elif user == comp:
        print("Draw!")
    elif (user == "Snake" and comp == "Water") or \
        (user == "Water" and comp == "Gun") or \
        (user == "Gun" and comp == "Snake"):
        user_score += 1
        print("You Won!")
    else:
        print("You Lose!")
        com_score += 1
    i+=1

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\Scores.txt", "w") as f:

    f.write(f"Your score : {user_score}, Computer score : {com_score}")

    