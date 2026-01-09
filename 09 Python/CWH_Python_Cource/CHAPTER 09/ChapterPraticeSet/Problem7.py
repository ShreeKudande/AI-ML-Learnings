#Q.Write a program to find out the line number where python is present from ques 6.

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\log.html") as f:
    lines = f.readlines()

line_no = 1
for line in lines:
    if "python" in line:
        print(f"This word is present. Line no : {line_no}")
        break
    line_no += 1
else:
    print("This word is not present in log.html")
            