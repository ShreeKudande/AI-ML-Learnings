#Q.Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
odd = ()
even = ()

for i in numbers:
    if i % 2 == 0:
        even = even + (i,)
    elif i % 2 != 0:
        odd = odd + (i,)

print(f"Odd : {odd} Even : {even}")

