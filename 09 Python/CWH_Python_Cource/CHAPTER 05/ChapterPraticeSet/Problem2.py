#Q.Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()
for i in range(9):
    user = int(input(f"Enter Number {i} : "))
    s.add(user)

print(s)
