#Q. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dict = {}

for i in range(1,5):
    user_key = input(f"Friend {i} name : ")
    user_value = input(f"Friend {i} fav-lang : ")
    dict.update({user_key:user_value})

print(dict)

