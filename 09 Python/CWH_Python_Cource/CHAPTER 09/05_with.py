# f = open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\file.txt")
# data = f.read()
# print(data)
# f.close()

#same can be done using with
with open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\file.txt") as f:
    print(f.read())

# You don't have to close file explicitly using f.close()