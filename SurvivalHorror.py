#!/usr/bin/env python3

# Script Name:      Survival Horror
# Author:           Vincent Bailey
# Last Rev:         03/23/2023
# Purpose:          This is a text-based game based on a survival horror
#                   classic.

##############################################################################
# Libraries
##############################################################################
import pygame, random, time, sys


##############################################################################
# Classes
##############################################################################
# STARS
class Redfield(object):
    health = 150
    strength = 15
    defense = 10
    resolve = 8


class Valentine(object):
    health = 150
    strength = 18
    defense = 10
    resolve = 5


# Enemy
class Beast(object):
    name = "Tyrant"
    health = 40
    strength = 35
    defense = 20
    loot = random.randint(0, 2)


class Zombie(object):
    name = "Zombie"
    health = 30
    strength = 15
    defense = 20
    loot = random.randint(0, 2)


class Dog(object):
    name = "Cerberus"
    health = 20
    strength = 10
    defense = 20
    loot = random.randint(0, 2)


class Licker(object):
    name = "Licker"
    health = 35
    strength = 20
    defense = 20
    loot = random.randint(0, 2)


##############################################################################
# Game Over Function
##############################################################################
def game_over(character, player_score):
    if character.health < 1:
        print("YOU ARE DEAD")
        time.sleep(2.4)
        print("You earned ", player_score,". Not bad.")
        time.sleep(2.4)
        print("Thank you for playing.")
        time.sleep(2.4)
        exit()


##############################################################################
# Character Select Function
##############################################################################
def hero_select():
    print("Select Your Hero")
    selection = input("1. Redfield \n2. Valentine \n\n")

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
        hero_select()


##############################################################################
# Enemy Select Function
##############################################################################
def enemy_select(Beast, Zombie, Dog, Licker):
    enemy_list = [Beast, Zombie, Dog, Licker]
    spawn = random.randint(0, 2)
    enemy = enemy_list[spawn]
    return enemy


##############################################################################
# Loot Function
##############################################################################
def loot():
    loot = ["Handgun Bullets", "Combat Knife", "First Aid Spray"]
    loot_chance = random.randint(0, 2)
    loot_drop = loot[loot_chance]
    return loot_drop


##############################################################################
# Battle Function
##############################################################################
def battle_state(player_score):
    enemy = enemy_select(Beast, Zombie, Dog, Licker)
    print("A", enemy.name, "leapt out at you!")
    time.sleep(1.4)
    print("What are you going to do....")
    while enemy.health > 0:
        choice = input("1. Shoot\n2. Swing Combat Knife\n3. Run\n\n")

        # Option 1
        if choice == "1":
            print("You raise your trusty handgun and fire at the", enemy.name)
            hit_chance = random.randint(0, 10)
            if hit_chance > 3:
                enemy.health = enemy.health - character.strength
                print("Nice! A solid hit! The", enemy.name, "is now", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defense)
                    print("The", enemy.name, "strikes at you...")
                    time.sleep(1.4)
                    print("Your health dropped to", character.health)
                    time.sleep(2.4)
                    game_over(character, player_score)

                else:
                    if enemy.name == "Tyrant":
                        enemy.health = 200
                        player_score = player_score + 20
                        return player_score

                    elif enemy.name == "Zombie":
                        enemy.health = 100
                        player_score = player_score + 15
                        return player_score

                    elif enemy.name == "Cerberus":
                        enemy.health = 80
                        player_score = player_score + 10
                        return player_score

                    elif enemy.name == "Licker":
                        enemy.health = 100
                        player_score = player_score + 10
                        return player_score

                    print("Always aim for the head! The", enemy.name, "is down!")
                    time.sleep(1.4)
                    print("Looks like it dropped something....")
                    time.sleep(1.4)
                    loot_drop = loot()
                    print("You picked up", loot_drop, "from the corpse.")
                    break

            else:
                print("Damn you missed....")
                time.sleep(1.4)
                print("The", enemy.name, "hits you for full damage.")
                character.health = character.health - enemy.strength
                print("Your health is at", character.health, "now.")
                time.sleep(2.4)
                game_over(character, player_score)

        # Option 2
        if choice == "2":
            print("You unsheathe your combat knife and take a forceful swing at the", enemy.name)
            hit_chance = random.randint(0, 10)
            if hit_chance > 3:
                enemy.health = enemy.health - character.resolve
                print("You cut a deep gash across the", enemy.name, "'s face. It's health is now", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defense)
                    print("The", enemy.name, "strikes at you...")
                    time.sleep(1.4)
                    print("Your health dropped to", character.health)
                    time.sleep(2.4)
                    game_over(character, player_score)

                else:
                    if enemy.name == "Tyrant":
                        enemy.health = 200
                        player_score = player_score + 20
                        return player_score

                    elif enemy.name == "Zombie":
                        enemy.health = 100
                        player_score = player_score + 15
                        return player_score

                    elif enemy.name == "Cerberus":
                        enemy.health = 80
                        player_score = player_score + 10
                        return player_score

                    elif enemy.name == "Licker":
                        enemy.health = 100
                        player_score = player_score + 10
                        return player_score

                    print("A messy but effective beheading! The", enemy.name, "is down!")
                    time.sleep(1.4)
                    print("Looks like it dropped something....")
                    time.sleep(1.4)
                    loot_drop = loot()
                    print("You picked up", loot_drop, "from the corpse.")
                    break

            else:
                print("Damn you missed....")
                time.sleep(1.4)
                print("The", enemy.name, "hits you for full damage.")
                character.health = character.health - enemy.strength
                print("Your health is at", character.health, "now.")
                time.sleep(2.4)
                game_over(character, player_score)

        # Option 3
        if choice == "3":
            print("You try to run....")
            run_chance = random.randint(0, 10)
            if run_chance > 4:
                print("You got away unscathed!")
                break
            else:
                print("You try to run but you slip and fall!")
                time.sleep(1.6)
                print("You back away quickly but the", enemy.name, "takes a bite out of your chest.")
                character.health = character.health - enemy.strength
                time.sleep(1.6)
                print("You kick the", enemy.name, "off of you and steady yourself.")
                time.sleep(2.4)
                game_over(character, player_score)

        # Any other option
        else:
            print("Please select either 1, 2, or 3 to perform an action.")


##############################################################################
# Main
##############################################################################
player_score = 0
character = hero_select()
player_score = battle_state(player_score)
battle_state(player_score)
print(player_score)
##############################################################################
# End
##############################################################################
