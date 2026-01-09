#Q.Repeat program 4 for a list of such words to be censored.

word = ["Donkey", "Nikhil", "Vivak"]

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\list.txt", "r") as f:

    content = f.read()

    for word in word:
        content = content.replace(word, "#" * len(word))

with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\ChapterPraticeSet\list.txt", "w") as f:
    f.write(content)
