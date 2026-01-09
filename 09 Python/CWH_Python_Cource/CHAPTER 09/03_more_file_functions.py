f = open(r"C:\Users\shree\Desktop\Python\CWH_Python_Cource\CHAPTER 09\file.txt", "r")

# lines = f.readlines()
# print(lines, type(lines))

line1 = f.readline()
line2 = f.readline()
print(line1, line2, type(line1))
f.close()
