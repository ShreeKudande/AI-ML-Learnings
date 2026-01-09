#A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\donkey.txt", "r") as f:

    content = f.read()

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\donkey.txt", "w") as f:

    new_content = content.replace(word, "#####")
    f.write(new_content)
