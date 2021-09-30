# Author: Brandon Petersen
# Date: November 6 2017
# Problem: This program is a text adventure game. Users play the part of a discoverer going on a journey to map out
# America so it can be settled. The traveler needs to manage their supplies and make choices while weighing in the
# consequences of their actions. Users can choose from the following actions: Travel, which moves the explorer towards
# their goal of finishing their map, explore, which allows you to find locations, items, and more at each stop,
# inventory, which allows user to see everything they are carrying, and quit, which allows you to leave the game.
# This game has randomly generated length, and events, so every time you play the game, it will be different.
# If you finish the game, play again and see how many forts, springs, indian camps, caves, and more that you can
# discover. Do you have what it takes to be the world's greatest explorer?
# Title: MANIFEST DESTINY: FRONTIER EXPLORER v 0.5

# Pseudocode
# Start
# Introduce game
# Ask user for name and if they want to play
# Generate random list of supplies
# Game loop
# Count steps when repeating loop
# Give option for travel
# Give option to explore
# Give option for inventory
# Give option to quit
# Create random scenario generator
# Create random events for exploring
# Create mid-point notification
# Create Game over situations
# Display results of game
# End

# Start Program

# Import modules from library
from random import randint
import random
import os

# Mythical Monsters
monsters = []

# Landmarks mapped/survived
landmarks = []

# Random generated supply list that is then sorted
generatesupplies = ["food", "medicine", "horses", "water", "clothing", "ammunition", "wagon parts"]
supplies = []
tradesupplies = ["food", "medicine", "horses", "clothing", "ammunition", "wagon parts"]
for x in range(1, 11):
    supplies.append(random.choice(generatesupplies))

# Generated checkpoints with calculated stops
checkpoints = randint(20, 30)
checkpoint = int(0)
midpoint = round(checkpoints / 2)

# Title screen
os.system('cls')
print("           MANIFEST DESTINY: FRONTIER EXPLORER")
print("                       version 0.5")
print("                   by Brandon Petersen")
print("                                       --")
print("               v            v       /      \ ")
print("                                    \      /")
print("           ^            v              --")
print()
print("               /\ ")
print("              /  \       /\ ")
print("             /     \    /  \ ")
print("       /\   /       \  /    \ ")
print("      /  \ /         \/      \    /\              .")
print("     /    \          /        \  /  \            /|\ ")
print("    /      \                   \/    \          /|||\ ")
print("   /               000000       \     \        /|||||\ ")
print("  /   00         00000000000     \     \      /|||||||\ ")
print(" /  00000     00000000000000000   \     \        | |   ")
print("00000000000000000000000000000000000000000000000000000000")
print()
print("                -PRESS ENTER TO CONTINUE-")
anykey1 = input()
os.system('cls')


# Game heading graphic
def callbanner():
    os.system('cls')
    print("-----------------------------------------------------")
    print("      MANIFEST DESTINY: FRONTIER EXPLORER v 0.5     ")
    print("                by Brandon Petersen                 ")
    print("-----------------------------------------------------")
    print()


# Introduction screen
callbanner()
print("The new world has successfully populated 13 colonies.")
print("Many people want to set out west and start their new lives.")
print("The land is rough with many unknown dangers.")
print("Some explorers have traveled to map and journal their findings.")
print()
anykey2 = input("Press ENTER to continue.")
os.system('cls')


callbanner()
print("You decide you want to join the effort.")
print("What a great adventure it would be to discover the undiscovered.")
print("Supplies are scarce, but you gather what you can for your journey.")
print("You leave your family and friends to start your adventure.")
print()

anykey3 = input("Press ENTER to continue.")
os.system('cls')

callbanner()

# Game started ready to play and user name input
gameon = input("Ready to start your journey? Y or N?")
if gameon.lower() == "y":
    name = input("What is your name?")
    name = name.upper()
    os.system('cls')
    callbanner()
    print(name, "you are ready to begin your journey.")
else:
    callbanner()
    print("You suddenly have second thoughts and")
    print("shamefully never started your adventure.")
    print("You go into hiding and and are alone")
    print("for the rest of your days.")
    print()

# While loop for gameplay
while gameon.lower() == "y":
    # Command display for player
    print()
    print("-----------------------------------------------------")
    print("COMMANDS: 'travel', 'explore', 'inventory', or 'quit'")
    print("-----------------------------------------------------")
    option = input("What would you like to do?")

# Called function for explore command
    def callexplore():
        game = ["bear", "elk", "mountain lion", "squirrel", "turkey", "deer", "antelope", "buffalo", "moose", "rabbit",
                "badger", "beaver", "raccoon", "bighorn sheep", "bison", "fox", "pheasant"]
        callbanner()
        roll = randint(1, 15)

        if roll == 7:
            tribe = input("You have discovered an indian camp! Do you wish to enter? Y or N?")
            if tribe.lower() == "y":
                callbanner()
                roll = randint(1, 4)
                if roll == 1:
                    callbanner()
                    print("The indians felt threatened by your presence and attack.")
                    supplies[:] = []
                else:
                    callbanner()
                    print("The indians are peaceful. They invite you to visit and share supplies.")
                    supplies.append(random.choice(generatesupplies))
                    landmarks.append("Indian Camp(s)")
            else:
                callbanner()

                print("You sneak past the camp unnoticed.")

        elif roll == 8:
            callbanner()
            wagon = input("You have found an abandoned wagon! Do you wish to search? Y or N?")
            if wagon == "y":
                roll = randint(1, 4)
                if roll == 1:
                    callbanner()
                    print("It's a trap! Bandits used the wagon as bait to draw you in for an attack.")
                    supplies[:] = []
                else:
                    callbanner()
                    supplies.append("wagon parts")
                    print("You find some useful spare wagon parts.")
            else:
                callbanner()
                print("Abandoned wagons can be dangerous.")

        elif roll == 9:
            callbanner()
            cave = input("You have found a secret cave! Do you wish to enter? Y or N?")
            if cave.lower() == "y":
                roll = randint(1, 4)
                if roll == 1:
                    callbanner()
                    print("You were surprise attacked by a bear.")
                    supplies[:] = []
                else:
                    callbanner()
                    print("You have found some supplies.")
                    supplies.append(random.choice(generatesupplies))
                    landmarks.append("Cave(s)")
            else:
                callbanner()

                print("Unexplored caves can be dangerous.")

        elif roll == 10:
            callbanner()
            fort = input("You have found an abandoned fort!  Do you wish to enter? Y or N?")
            if fort.lower() == "y":
                roll = randint(1, 4)
                if roll == 1:
                    os.system('cls')
                    callbanner()
                    print("The abandoned fort is a hideout for bandits. You are surprise-attacked.")
                    supplies[:] = []
                else:
                    os.system('cls')
                    callbanner()
                    print("You have found some supplies")
                    supplies.append(random.choice(generatesupplies))
                    landmarks.append("Fort(s)")
            else:
                callbanner()
                print("Abandoned forts can be dangerous.")

        elif roll == 11:
            callbanner()
            lake = input("You have found a natural spring! Do you wish to swim? Y or N?")
            if lake.lower() == "y":
                os.system('cls')
                callbanner()
                print("You feel refreshed, and replenish your water supply.")
                landmarks.append("Spring(s)")
                supplies.append("water")
            else:
                os.system('cls')
                callbanner()
                print("Untested waters can be dangerous.")

        elif roll == 12:
            callbanner()
            furtrapper = input("You have encountered some fur trappers. Do you wish to talk? Y or N?")
            if furtrapper.lower() == "y":
                roll = randint(1, 4)
                if roll == 1:
                    os.system('cls')
                    callbanner()
                    print("The fur trappers are suspicious of you and open fire.")
                    supplies[:] = []
                else:
                    os.system('cls')
                    callbanner()
                    print("The fur trappers are friendly and share their campfire, company, and ammunition.")
                    supplies.append("ammunition")
            else:
                callbanner()
                print("You wave as you pass by the fur trappers.")

        elif roll == 13:
            callbanner()
            print("You come across a stranger who is low on water and is willing to trade.")
            trade = input("Trade 1 water for supplies? Y or N?")
            if trade.lower() == "y" and "water" in supplies:
                callbanner()
                print("You trade with the stranger, and probably saved his life.")
                print("1 water has been removed, and 1 supplies has been added.")
                supplies.remove("water")
                supplies.append(random.choice(tradesupplies))
            else:
                callbanner()
                print("You either don't have water or you don't want to trade.")

        elif roll == 14:
            callbanner()
            print("You have tracked down a", random.choice(game), ".")
            hunt = input("Would you like to hunt it? Y or N?")
            if hunt.lower() == "y" and "ammunition" in supplies:
                roll = randint(1, 3)
                if roll == 1:
                    callbanner()
                    print("You missed, and it got away.")
                    print("1 ammunition has been removed.")
                    supplies.remove("ammunition")
                else:
                    callbanner()
                    print("Great shot!")
                    print("You are able get food and clothing from your hunt.")
                    print("1 ammunition has been removed.")
                    supplies.remove("ammunition")
                    supplies.append("food")
                    supplies.append("clothing")
            else:
                callbanner()
                print("You either don't have time or ammunition for hunting right now.")

        elif roll == 15 and checkpoint == randint(1, 3):
            callbanner()
            mothmanencounter = input("You have encountered The Mothman! Do you wish to pursue? Y or N?")
            if mothmanencounter.lower() == "y" and "ammunition" in supplies:
                roll = randint(1, 4)
                if roll == 1:
                    callbanner()
                    print("The Mothman got away.")
                    print("1 ammunition has been removed.")
                    supplies.remove("ammunition")
                else:
                    callbanner()
                    print("You have successfully hunted The Mothman!")
                    monsters.append("The Mothman")
                    print("1 ammunition has been removed.")
                    supplies.remove("ammunition")
            elif mothmanencounter.lower() == "n":
                callbanner()
                print("The Mothman sees you, then quickly flies away.")
            else:
                callbanner()
                print("You have angered the Mothman and have no ammunition.")
                print("The Mothman carries you away, and you are never seen again.")
                supplies[:] = []

        elif roll == 15 and checkpoint == randint(10, 15):
            callbanner()
            alkalilakecounter = input("You have encountered The Alkali Lake Monster! Do you wish to pursue? Y or N?")
            if alkalilakecounter.lower() == "y" and "ammunition" in supplies:
                roll = randint(1, 4)
                if roll == 1:
                    callbanner()
                    print("The Alkali Lake Monster got away.")
                    print("1 ammunition has been removed.")
                    supplies.remove("ammunition")
                else:
                    callbanner()
                    print("You have successfully hunted the Alkali Lake Monster!")
                    print("1 ammunition has been removed.")
                    monsters.append("The Alkali Lake Monster")
                    supplies.remove("ammunition")
            elif alkalilakecounter.lower() == "n":
                callbanner()
                print("The Alkali Lake Monster sees you, then quickly swims away.")
            else:
                callbanner()
                print("You have angered the Alkali Lake Monster and have no ammunition.")
                print("The Alkali Lake Monster pulls you under water, and you are never seen again.")
                supplies[:] = []

        elif roll == 15 and checkpoint == randint(18, 19):
            callbanner()
            bigfootencounter = input("You have encountered Bigfoot! Do you wish to pursue? Y or N?")
            if bigfootencounter.lower() == "y" and "ammunition" in supplies:
                roll = randint(1, 4)
                if roll == 1:
                    callbanner()
                    print("Bigfoot got away.")
                    supplies.remove("ammunition")
                    print("1 ammunition has been removed.")
                else:
                    callbanner()
                    print("You have successfully hunted Bigfoot!")
                    print("1 ammunition has been removed.")
                    monsters.append("Bigfoot")
                    supplies.remove("ammunition")
            elif bigfootencounter.lower() == "n":
                callbanner()
                print("Bigfoot sees you, then quickly runs away.")
            else:
                callbanner()
                print("You have angered Bigfoot and have no ammunition.")
                print("Bigfoot carries you away, and you are never seen again.")
                supplies[:] = []

        else:
            roll2 = randint(1, 10)
            if roll2 == 1:
                print("You find a scenic look over a quiet meadow.")
            elif roll2 == 2:
                print("You see some animal tracks.")
            elif roll2 == 3:
                print("You see a unique rock formation.")
            elif roll2 == 4:
                print("It looks like someone had a camp fire here a few days ago.")
            elif roll2 == 5:
                print("You find some arrowheads.")
            elif roll2 == 6:
                print("You see some tipi rings.")
            elif roll2 == 7:
                print("This looks like a good place to hunt.")
            elif roll2 == 8:
                print("You find some fun rocks to climb.")
            elif roll2 == 9:
                print("You hear some wolves howling in the distance.")
            else:
                print("You find nothing.")

# Called function for random scenarios generated
    def scenariosgenerate():
        callbanner()

        scenarioslist = ["food", "lost", "nothing", "nothing2", "nothing3", "rattlesnake", "dysentery", "bandit",
                         "stuck", "wagon", "hunt", "broken", "horses", "axle", "yoke", "fort1", "fort2", "lake",
                         "settlers", "stranger", "trade", "snow"]

        scenarios = random.choice(scenarioslist)

        if scenarios == "snow":
            print("It has been snowy and cold. You have worn out some of your clothing.")
            if "clothing" in supplies:
                print("You are able to change into warmer and more durable clothing.")
                print("1 clothing has been removed.")
                supplies.remove("clothing")
            else:
                print("You don't have any more clothing and freeze to death.")
                supplies[:] = []

        if scenarios == "trade":
            print("You come across a stranger who is low on water and is willing to trade.")
            trade = input("Trade 1 water for supplies? Y or N?")
            if trade.lower() == "y" and "water" in supplies:
                callbanner()
                print("You trade with the stranger, and probably saved his life.")
                print("1 water has been removed, and 1 supplies has been added.")
                supplies.remove("water")
                supplies.append(random.choice(tradesupplies))
            else:
                callbanner()
                print("You either don't have water or you don't want to trade.")

        if scenarios == "settlers":
            print("You come across a family of settlers. You help them with their chores.")
            print("In return, the settlers invite you in for the night and share supplies for your journey.")
            supplies.append(random.choice(generatesupplies))

        if scenarios == "food":
            print("You are starving and need something to eat.")
            if "food" in supplies:
                print("You eat some very delicious beef jerky.")
                supplies.remove("food")
                print("1 food has been removed.")
            else:
                print("You don't have any more food and you starve to death.")
                supplies[:] = []

        if scenarios == "lost":
            print("You are lost.")
            if "water" in supplies:
                print("You found your way back.")
                supplies.remove("water")
                print("1 water has been removed.")
            else:
                print("You are out of water and die of dehydration.")
                supplies[:] = []

        if scenarios == "lake":
            print("You have found a natural spring.")
            supplies.append("water")
            print("You replenish your water supply.")
            landmarks.append("Spring(s)")

        if scenarios == "fort1":
            print("You have found a fort. The soldiers share some supplies.")
            supplies.append(random.choice(generatesupplies))
            landmarks.append("Fort(s)")

        if scenarios == "fort2":
            print("You have found a fort. The soldiers share some supplies.")
            supplies.append(random.choice(generatesupplies))
            landmarks.append("Fort(s)")

        if scenarios == "nothing":
            print("You decide to take a moment to enjoy the nice afternoon.")

        if scenarios == "nothing2":
            print("A beautiful day of traveling with no calamities.")

        if scenarios == "nothing3":
            print("A rainy day brought a slow day of travel, but no incidents either.")

        elif scenarios == "rattlesnake":
            print("You have been bitten by a rattlesnake.")
            if "medicine" in supplies:
                supplies.remove("medicine")
                print("1 medicine has been removed.")
            else:
                print("You have no more medicine.")
                supplies[:] = []

        elif scenarios == "dysentery":
            print("You have contracted dysentery.")
            if "medicine" in supplies:
                supplies.remove("medicine")
                print("1 medicine has been removed.")
            else:
                print("You have no more medicine.")
                supplies[:] = []

        elif scenarios == "bandit":
            print("You have been attacked by bandits.")
            if len(supplies) > 0:
                supplies.remove(random.choice(supplies))
                print("The bandits escaped with some of your supplies.")
            else:
                print("The bandits stole your transportation and left you for dead.")
                supplies[:] = []

        elif scenarios == "stuck":
            print("Your wagon and transportation is stuck")
            roll = randint(1, 10)
            if roll < 9:
                print("You manage to free your transportation")
                if len(supplies) > 0:
                    supplies.remove(random.choice(supplies))
                    print("1 wagon parts have been removed.")
                else:
                    print("You have used the rest of your supplies and can go no further.")

            elif roll > 8:
                print("You are unable to free your transportation.")
                print("You are stranded alone for the rest of your days.")
                supplies[:] = []

        elif scenarios == "wagon":
            print("You have found an abandoned wagon.")
            supplies.append(random.choice(generatesupplies))
            print("You picked up some extra supplies.")

        elif scenarios == "hunt":
            print("You have tracked down a wild beast.")
            if "ammunition" in supplies:
                roll = randint(1, 10)
                if roll < 7:
                    print("You successfuly shot and killed the beast!")
                    print("You have collected food and make clothing from the hide.")
                    print("1 ammunition has been removed.")
                    supplies.append("food")
                    supplies.append("clothing")
                    supplies.remove("ammunition")
                else:
                    print("You fired at the beast but missed.")
                    print("The beast is scared away.")
                    print("1 ammunition has been removed.")
                    supplies.remove("ammunition")
            else:
                print("The beast charges you, but you have no ammunition to protect yourself.")
                print("You are injured.")
                if "medicine" in supplies:
                    supplies.remove("medicine")
                    print("1 medicine has been removed.")
                else:
                    print("You have no more medicine.")
                    supplies[:] = []

        elif scenarios == "horses":
            print("A horse is sick or injured.")
            if "horses" in supplies:
                supplies.remove("horses")
                print("1 horses has been removed.")
            else:
                print("You have no more horses.")
                print("You are stranded alone for the rest of your days.")
                supplies[:] = []

        elif scenarios == "broken":
            print("You fell and broke a bone.")
            if "medicine" in supplies:
                supplies.remove("medicine")
                print("You were able to heal your injury.")
                print("1 medicine has been removed.")
            else:
                print("You were unable to heal your injury.")
                supplies[:] = []

        elif scenarios == "axle":
            print("Your wagon has suffered a broken axle.")
            if "wagon parts" in supplies:
                supplies.remove("wagon parts")
                print("You were able to fix the broken axle.")
                print("1 wagon parts has been removed.")
            else:
                print("You are out of spare parts to fix your wagon.")
                print("You are stranded alone for the rest of your days.")
                supplies[:] = []

        elif scenarios == "yoke":
            print("Your wagon has suffered a broken yoke.")
            if "wagon parts" in supplies:
                supplies.remove("wagon parts")
                print("You were able to fix the yoke.")
                print("1 wagon parts has been removed.")
            else:
                print("You are out of spare parts to fix your wagon.")
                print("You are stranded alone for the rest of your days.")
                supplies[:] = []

        elif scenarios == "stranger":
            print("A stranger runs towards you. He gives you supplies, and hurries off")
            print("as if he's in trouble. These will be useful on your journey.")
            supplies.append(random.choice(generatesupplies))

# Commands from user
    if option.lower() == "inventory":
        callbanner()
        print("Here is your current list of supplies:")
        list.sort(supplies)
        print(supplies)

    elif option.lower() == "explore":
        os.system('cls')
        callexplore()

    elif option.lower() == "travel":
        os.system('cls')
        checkpoint = checkpoint + 1
        scenariosgenerate()

    elif option.lower() == "quit":
        callbanner()
        print("You leave the adventure and explorer life and settle down")
        print("by living the solitary life of a mountain man.")
        gameon = "n"

    else:
        callbanner()
        print("I do not understand that command.")

# Checkpoint and game progress
    if checkpoint == midpoint:
        print()
        print("Way to go", name, "!  You have made it to chimney rock!")
        print("You are half-way there!")
        print("                                       --")
        print("                                    /      \ ")
        print("                                    \      /")
        print("                                       --")
        print("                           ")
        print("                              0    ")
        print("                 ________    00                   ")
        print("              __/        \__ 00_____         ")
        print("          ___/               00     \_          ")
        print("         /                 0000       \_    ")
        print("        /               000000000       \  ")
        print("       /          000000000000000000     \     ")
        print("00000000000000000000000000000000000000000000000000000000")

# Win game takes out of loop
    if checkpoint == checkpoints:
        print("Congratulations", name, "! Your adventure is over!")
        print("Map of your journey:")
        print()
        print("  ---\/ --------------------\__           ___/--| ")
        print("  |                           \_    ____/     | ")
        print("  \  X_ _ _                     \__/       _/ ")
        print("  /         \                        _X  / ")
        print("  |          \_ _ _ _ _     / \ _ _ /   / ")
        print("   \                     \ /            | ")
        print("    |                                   / ")
        print("     \__                               / ")
        print("        \______/--\          ____/--| / ")
        print("                   \_/-\    /      |  | ")
        print("                        \-_|        \_| ")
        print()
        print("Your findings paved the way for pioneers to settle all across America!")
        print("You are a legend in your own time!")
        gameon = "n"

# Lose game takes out of loop
    if len(supplies) == 0:
        print()
        print("You have died,", name, ".")
        print("            ____________________________ __ ")
        print("          /                              \  \ ")
        print("         /                                \  \ ")
        print("        |                                  |  | ")
        print("        |    XXXXX       X      X XXXX     |  | ")
        print("        |    X    X      X      X     X    |  | ")
        print("        |    XXXXX       X      XXXXXX     |  | ")
        print("        |    X    X      X      X          |  | ")
        print("        |    X     X     X      X          |  | ")
        print("        |                                  |  | ")
        print("        |                                  |  | ")
        print("        | 'Man cannot discover new oceans  |  | ")
        print("        |    unless he has the courage     |  | ")
        print("        |    to lose sight of the shore.'  |  | ")
        print("        |                 -Andre Gide      |  | ")
        print("    0000|                                  |  |000000")
        print("  0000000000000000000000000000000000000000000000000000")
        print("00000000000000000000000000000000000000000000000000000000")
        print()
        gameon = "n"

# Results of game
if checkpoint > 29:
    print("You have set the new standard. All other explorers wish they were you.")
elif checkpoint > 19:
    print("You were one of the most famous explorers in America.")
elif checkpoint > 10:
    print("Strangers you met on your travels will tell stories of your adventures.")
elif checkpoint > 5:
    print("Your friends and family will tell stories of your adventures for years to come.")
else:
    print("Your friends and family will miss you very much.")

if len(landmarks) > 0:
    print()
    print("You have mapped the following landmarks on your journey:")
    if checkpoint >= round(checkpoints / 2):
        print("Chimney Rock")
    if landmarks.count("Indian Camp(s)") > 0:
        print((landmarks.count("Indian Camp(s)"), "Indian Camp(s)"))
    if landmarks.count("Fort(s)") > 0:
        print((landmarks.count("Fort(s)"), "Fort(s)"))
    if landmarks.count("Cave(s)") > 0:
        print((landmarks.count("Cave(s)"), "Cave(s)"))
    if landmarks.count("Spring(s)") > 0:
        print((landmarks.count("Spring(s)"), "Spring(s)"))

monsters = set(monsters)
if len(monsters) > 0:
    print()
    print("You famously caught the following creature(s):")
    print(monsters)

print()
print("Your adventure lasted", checkpoint, "month(s).")
print("Game Over.")
print("----------------------------------------------------")

# Prevents exe version of file from closing window right at the end of the game
endgame = input("Press ENTER to quit.")

# End Program