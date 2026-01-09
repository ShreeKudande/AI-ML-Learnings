#Q.Ask the user for a string and print:
#All unique characters
#The count of unique characters

user = input("Type something : ")

s = set(user)

print("Unique characters:", s)
print("Count:", len(s))

