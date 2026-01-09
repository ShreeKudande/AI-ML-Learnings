# f(n) = f(n-2) + f(n-1) --> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,

n = 10
a = 0 
b = 1

for i in range(n-2):
    c = a + b
    print(c)

    a = b
    b = c
