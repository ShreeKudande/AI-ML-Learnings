friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)

friends.append("Shree")
print(friends)

# ['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan']
# ['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan', 'Shree']

ls = [6, 5, 1, 60, 23, 65, 30, 25, 15, 4, 5, 10]
ls.sort() #[1, 4, 5, 5, 6, 10, 15, 23, 25, 30, 60, 65]
ls.reverse() #[65, 60, 30, 25, 23, 15, 10, 6, 5, 5, 4, 1]

ls.insert(3, 30000) #[65, 60, 30, 30000, 25, 23, 15, 10, 6, 5, 5, 4, 1]
ls.pop(3) #[65, 60, 30, 25, 23, 15, 10, 6, 5, 5, 4, 1]

ls.remove(5)
ls.remove(1)
#[65, 60, 30, 23, 15, 10, 6, 5, 4]


print(ls.pop(3)) #25

ls.clear() # []
print(ls)




