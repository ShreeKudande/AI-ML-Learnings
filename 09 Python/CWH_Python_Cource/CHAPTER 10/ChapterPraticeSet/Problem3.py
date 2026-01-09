#Q.Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a = 1

obj = demo()
print(obj.a)
obj.a = 0
print(obj.a)
print(demo.a)

# No it does not change the class attribute


