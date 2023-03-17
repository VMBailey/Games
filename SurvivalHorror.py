##############################################################################
# Libraries
##############################################################################
import pygame, random, time, sys

##############################################################################
# Classes
##############################################################################
## STARS
class Redfield (object):
    health = 150
    strength = 10
    defense = 10
    resolve = 15

class Valentine (object):
    health = 150
    strength = 8
    defense = 10
    resolve = 15
    
## Enemy
class Beast (object):
    name = "Nemesis"
    health = 200
    strength = 15
    defense = 20
    loot = random.randint(0,2)

class Zombie (object):
    name = "Tattered"
    health = 100
    strength = 15
    defense = 20
    loot = random.randint(0,2)

class Dog (object):
    name = "Zombie Dog"
    health = 80
    strength = 15
    defense = 20
    loot = random.randint(0,2)

class Licker (object):
    name = "Licker"
    health = 100
    strength = 15
    defense = 20
    loot = random.randint(0,2)

##############################################################################
# Character Select Function
##############################################################################
def heroselect():
    print("Select Your Hero")
    selection = input("1. Redfield \n2. Valentine \n")

    if selection == "1":
        character = Redfield
        print("Welcome to Arkham Manor, Mr. Redfield. Here are your stats.")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Resolve - ", character.resolve)
        return character
    
    elif selection == "2":
        character = Valentine
        print("Welcome to Arkham Manor, Ms. Valentine. Here are your stats.")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Resolve - ", character.resolve)
        return character
    
    elif selection == "3":
        print("Until Next Time.....")
        time.sleep(1.6)
        sys.exit()
    
    else:
        print("Please enter either 1 or 2 to select a character.")
        time.sleep(1.4)
        heroselect()

##############################################################################
# Enemy Select Function
##############################################################################
def enemyselect(Beast,Zombie,Dog,Licker):
    enemyList = [Beast,Zombie,Dog,Licker]
    spawn = random.randint(0,2)
    enemy = enemyList[spawn]
    return enemy

##############################################################################
# Loot Function
##############################################################################
def loot():
    loot = ["Handgun Bullets", "Combat Knife", "First Aid Spray"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

##############################################################################
# Main
##############################################################################
heroselect()
##############################################################################
# End
##############################################################################