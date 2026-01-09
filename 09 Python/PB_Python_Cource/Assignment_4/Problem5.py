#Q.Creat a base class Vehicle with attributes like brand and model. Create two subclasses Car and Bike that add extra attibutes - seats (in Car) & engine_cc (in Bike).

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):

    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    
    def __init__(self, brand, model, engine__cc):
        super().__init__(brand, model)
        self.engine__cc = engine__cc


c1 = Car("Toyota", "Fortuner", 7)
b1 = Bike("Royal_Enfield", "Meteor_Fireball", 350)

print(c1.brand, c1.model, c1.seats)
print(b1.brand, b1.model, b1.engine__cc)

