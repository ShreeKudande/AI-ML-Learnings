#Q.Create a program that:
# 1. Opens a file "log.txt" in append mode
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs

file_path = r"D:\Python\PB_Python_Cource\Assignment_5\log.txt"

with open(file_path, "a") as f:

    new_entry = f.write("\nProgram run successfully")

with open(file_path, "r") as f:
    logs = f.read()
    print(logs)