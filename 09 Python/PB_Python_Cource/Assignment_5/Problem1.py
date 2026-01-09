#Q.Create a program that: 
# 1. Opens a file "names.txt" in write mode
# 2. Write 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

file_path = r"d:\Python\PB_Python_Cource\Assignment_5\names.txt"

with open(file_path, "w") as f:
    
    for i in range(5):
        user = input(f"Name {i+1} : ")
        f.write(user + "\n")
        
        
with open(file_path, "r") as f:
    data = f.read()
    print("\nNames in files : ")
    print(data)
