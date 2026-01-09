#Q.Given a list, print all elements that appear more than once in the list.

numbers = [1, 1, 5, 6, 4, 2, 5, 1, 5, 0, 0, 29, 38, 9, 9]

for n in set(numbers):
    if numbers.count(n) > 1:
        print(n)
