#Q.Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

class Programmer:
    Company = "Microsoft"

    def __init__(slf, name, id):
        slf.name = name
        slf.id = id

Pro1 = Programmer("Shree", 5454)
Pro2 = Programmer("Nea", 6464)

print(f"Programmer_1 = {Pro1.name, Pro1.id, Pro1.Company}")
print(f"Programmer_2 = {Pro2.name, Pro2.id, Pro2.Company}")
