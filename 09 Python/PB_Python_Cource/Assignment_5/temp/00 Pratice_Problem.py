with open(r"D:\Python\01 PB_Python_Cource\Assignment_5\trash.txt") as f:

    search_word = "Python"

    data = True
    line = 1

    while data:
        data = f.readline()

        main_string = data
        if search_word in main_string:
            print(f"word \"{search_word}\" found at line {line}")
            break
        
        line+=1

#Outputf :- word "Python" found at line 3
  

