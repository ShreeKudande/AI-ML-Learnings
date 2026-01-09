#Q.Create a class “Programmer” for storing information of few programmers working at Microsoft

class Programmer:
    Company = "Microsoft"

    def __init__(self, name, id):
        self.name = name
        self.id = id

Pro1 = Programmer("Shree", 5454)
Pro2 = Programmer("Nea", 6464)

print(f"Programmer_1 = {Pro1.name, Pro1.id, Pro1.Company}")
print(f"Programmer_2 = {Pro2.name, Pro2.id, Pro2.Company}")
