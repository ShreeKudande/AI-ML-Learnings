#Q.Write a program to mine a log file and find out whether it contains ‘python’. 

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\log.html") as f:
    content = f.read()

user = input("Enter word to search in log.html : ") #python

if user in content:
    print("This word is present in log.html")
else:
    print("This word is not present in log.html")
    