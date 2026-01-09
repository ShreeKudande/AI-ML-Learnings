#Q.Write a program to find out whether a file is identical & matches the content of another file.

with open(r"CWH_Python_Cource/CHAPTER 09/ChapterPraticeSet/this.txt", "r") as f:
    content1 = f.read()
    
with open(r"CWH_Python_Cource/CHAPTER 09/ChapterPraticeSet/copy_of_this.txt", "r") as f:
    content2 = f.read()

if content1 == content2:
    print("This two files content matched")
else:
    print("This two file content does not matched")
    