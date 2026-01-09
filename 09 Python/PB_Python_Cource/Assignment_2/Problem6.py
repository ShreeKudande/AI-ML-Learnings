#Q.Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

n1 = 2
n2 = 5

for i in range(1, 100+1):
    if i % 3 == 0 and i % 5 == 0:
      print(i)
#OutPut :-
# 15
# 30
# 45
# 60
# 75
# 90

