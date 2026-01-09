#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\poem.txt", "r") as f:
    data = f.read()
    if "twinkle" in data:
        print("The word \"twinkle\" is present in the poem.txt")
    else:
        print("The word \"twinkle\" is not present in the poem.txt")
