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
    name = "Tyrant"
    health = 40
    strength = 35
    defense = 20
    loot = random.randint(0,2)

class Zombie (object):
    name = "Zombie"
    health = 30
    strength = 15
    defense = 20
    loot = random.randint(0,2)

class Dog (object):
    name = "Cerberus"
    health = 20
    strength = 10
    defense = 20
    loot = random.randint(0,2)

class Licker (object):
    name = "Licker"
    health = 35
    strength = 20
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
        print("Welcome to the Spencer Mansion, Mr. Redfield. Here are your stats.")
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
# Battle Function
##############################################################################
def battlestate():
    enemy = enemyselect(Beast,Zombie,Dog,Licker)
    print("A", enemy.name, "lept out at you!")
    time.sleep(1.4)
    print("What are you going to do....")
    while enemy.health > 0:
        choice = input("1. Shoot\n2. Swing Combat Knife\n3. Run\n")

        if choice == "1":
            print ("You raise your trusty handgun and fire at the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("Nice! A solid hit! The", enemy.name, "is now", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defense)
                    print ("The", enemy.name, "strikes at you...")
                    time.sleep(1.4)
                    print ("Your health dropped to", character.health)
                
                else:
                    if enemy.name == "Tyrant":
                        enemy.health = 200

                    elif enemy.name == "Zombie":
                        enemy.health = 100

                    elif enemy.name == "Cerberus":
                        enemy.health = 80
                    
                    elif enemy.name == "Licker":
                        enemy.health = 100

                    print ("Always aim for the head! The", enemy.name, "is down!")
                    time.sleep(1.4)
                    print ("Looks like it dropped something....")
                    time.sleep(1.4)
                    lootDrop = loot()
                    print ("You picked up", lootDrop, "from the corpse.")
                    break

            else:
                print ("Damn you missed....")
                time.sleep(1.4)
                print ("The", enemy.name, "hits you for full damage.")
                character.health = character.health - enemy.strength
                print("Your health is at", character.health, "now.")
##############################################################################
# Main
##############################################################################
character = heroselect()
battlestate()
##############################################################################
# End
##############################################################################