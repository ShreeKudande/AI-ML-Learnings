#Q.Create the following classes: Herbivore, Carnivore, Omnivore with some attributes & methods. Then create a class Bear that inherits form all the above classes to showcase how multiple inheritance works.

class Harbivore:
    def __init__(self):
        self.eats_plants = True

    def plant_food(self):
        return "Eats Plants"
    

class Carnivore:
    def __init__(self):
        self.eats_meat = True

    def meat_food(self):
        return "Eats Meat"
    

class Omnivore:
    def __init__(self):
        self.eats_both = True

    def mixed_food(self):
        return "Eats both plants and meat"
    
class Bear(Harbivore, Carnivore, Omnivore):
    def __init__(self):
        Harbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)
        self.species = "Bear"
    
    def info(self):
        print(self.species, self.plant_food(), self.meat_food(), self.mixed_food())

b = Bear()

b.info()

