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


attack = 30
# Weapon for classes
if player_class == "W":
   player_weapon = input("Select your weapon:\n"
"A-A melee weapon and shield\n"
"T-Two-handed weapon\n")
   if player_weapon == "A":
       attack = attack + 15
       print(f"You have {attack} attack")
       print("You have selected a melee weapon and shield")
   else:
       attack = attack + 20
       print(f"You have {attack} attack")
       print("You have selected a two-handed weapon")

elif player_class == "M":
    player_weapon = input("Select your weapon:\n"
"B-Bow\n"
"S-Staff\n")
    if player_weapon == "B":
        attack = attack + 25
        print(f"You have {attack} attack")
        print("You have selected a bow weapon")
    else:
        attack = attack + 35
        print(f"You have {attack} attack")
        print("You have selected a staff")

elif player_class == "R":
    player_weapon = input("Select your weapon:\n"
"D-Dagger\n"
"H-Hammer\n")
    if player_weapon == "D":
        attack = attack + 20
        print(f"You have {attack} attack")
    else:
        attack = attack + 15
        print(f"You have {attack} attack")
        print("You have selected a hammer")



player = Player(f"{player_name}", {player_class}, "pistol", 100)
print(player)
