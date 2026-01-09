#Q.Write a function that takes two integers a and b and prints all even numbers between them(inclusive).

def even_numbers(a,b):
    count = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)
            count+=1

    print(f"There are {count} even numbers in between.")
    return

even_numbers(2,12)


