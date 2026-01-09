#Q.Write a program that tries to open "data.txt" in read mode. If the file does not exist, catch the exception and print "File not found!".

try:

    file_path = r"D:\Python\PB_Python_Cource\Assignment_5\data.txt"

    with open(file_path, "r") as f:

        read_data = f.read()
        print(read_data)

except FileNotFoundError:
    print("File not found!")

    