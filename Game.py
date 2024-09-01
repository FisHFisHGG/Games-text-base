player_name = input("Enter your name: ")

player_class = input("Select your class:\n"
"W-Warrior\n"
"M-Mage\n"
"R-Rogue\n")

class Player:
    def __init__(self, name, role, weapon, health):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.health = health

    def attack(self, alien):
        pass

    def weapon(self):
        pass

    def health(self):
        pass

    def player_role(self):
        pass

class Enemy:
    def __init__(self, name_e, health_e):
        self.name_e = name_e
        self.health_e = health_e

    def attack(self, player):
        pass

health = 100
# Health for classes
if player_class == "W":
    health = health + 25
    print(f"You have {health} health")
elif player_class == "M":
    health = health - 20
    print(f"You have {health} health")
elif player_class == "R":
    health = health + 10
    print(f"You have {health} health")


attack = 0

If player_class == "W"
    input("Select your weapon:\n"
"A-A melee weapon and shield\n"
"T-Two-handed weapon\n") 



player = Player(f"{player_name}", {player_class}, "pistol", 100)
print(player)
