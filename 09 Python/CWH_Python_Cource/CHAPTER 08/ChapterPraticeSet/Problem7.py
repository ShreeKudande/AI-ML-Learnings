#Q.Write a python function to remove a given word from a list ad strip it at the same time.

def rem(ls, word):
    for item in ls:
        return ls.remove(word)

ls = ["Shree", "Vivak", "Saurabh", "an"]

rem(ls, "an")
print(ls)
