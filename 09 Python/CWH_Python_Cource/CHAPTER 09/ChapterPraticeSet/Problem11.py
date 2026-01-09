#Q.Write a python program to rename a file to “renamed_by_ python.txt.
import os

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\renamed.txt", "r") as f:
    content = f.read()
    
with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\renamed_by_python.txt", "w") as f:
    f.write(content)

# os.remove(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\renamed.txt")