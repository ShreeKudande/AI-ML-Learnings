#Q.Write a program to make a copy of a text file “this. txt”

with open(r"CWH_Python_Cource/CHAPTER 09/ChapterPraticeSet/this.txt", "r") as f:
    content = f.read()

with open(r"CWH_Python_Cource/CHAPTER 09/ChapterPraticeSet/copy_of_this.txt", "w") as f:
    f.write(content)