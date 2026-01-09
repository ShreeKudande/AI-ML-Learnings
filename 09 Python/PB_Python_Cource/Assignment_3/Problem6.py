#Q.Given a list of words:

words = ["apple", "banana", "kiwi", "cherry", "mango"]

#Create a dictionary that maps each word to its length.
#Example {"apple" : 5, "banana" : 6, "kiwi": 4, ...}

d = {}

for fruit in words:
    d[fruit] = len(fruit)

print(d)
