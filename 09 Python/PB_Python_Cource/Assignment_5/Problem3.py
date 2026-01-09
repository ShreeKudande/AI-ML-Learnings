#Q.Create a program that:
# 1.Has a list of numbers: [5, 10, 15, 20, 25]
# 2.Uses list comprehension to create a new list with only numbers greater than 15
# 3.Prints the new list

numbers = [5, 10, 15, 20, 25]

new_list = [x for x in numbers if x > 15]

print(new_list)