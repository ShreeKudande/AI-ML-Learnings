#Q.Create a class Player with:
#a class variable player_count
#instance variable name and level
#Track how many players were created.

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1
    
    def display(self):
        print(f"Player : {self.name}, Level : {self.level}")


p1 = Player("Shree", 10)
p2 = Player("Saurabh", 11)

p1.display()
p2.display()

print(Player.player_count)


    