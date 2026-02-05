#-------------------------
#TEXT BASED ADVENTURE GAME
#-------------------------

#initializing player stats and variables
#also used for replay with base attributes
def original_stats():

    #players stats
    global health, attack
    health=20
    attack=3

    #inventory
    global has_iron_sword,has_steel_sword,has_diamond_sword,has_key,has_lockpick,has_potion
    has_iron_sword=False
    has_steel_sword=False
    has_diamond_sword=False
    has_key=False
    has_lockpick=False
    has_potion=False

    #skeleton friend
    global skeleton_helpful
    skeleton_helpful=False

#------------------
#MAIN MENU FUNCTION
def main_menu():
    while True:
        print("==============================")
        print("    BONE DEEP BAD DECISIONS")
        print("==============================")
        print("== every choice leaves a mark ==")
        print("\n1. Start New Game\n2. Quit")
        print("(enter number to select the choice)")
        choice=input("> ")
        if choice=="1":
            original_stats()
            intro()
        elif choice=="2":
            print("\nFarewell Traveler.")
            exit()
        else:
            print("\nThis choice leads nowhere.")

#--------------
#INTRO FUNCTION
def intro():
    global health
    health=20
    print("A fire crackles softly...")
    print("You seem to have gotten stuck in a dark dungeon while out on your travels.")
    print("Your torch is nearly burnt out...\nYou start a fire to stay warm and regain energy.")
    print("\n** ALL STATS REPLENISHED **")
    print("Health:", health)
    print("Attack:", attack)
    print("\n** QUEST UPDATED: ESCAPE THE DUNGEON **")
    skeleton_encounter()
    next_choice()
 
#---------------------------
#SKELETON ENCOUNTER FUNCTION
def skeleton_encounter():
    global skeleton_helpful, health
    print("\nAs the fire continues to brighten your surroundings, you suddenly hear shuffling.")
    print("Glancing around you see a skeleton slouched in the corner reading a book.")
    print("As you stare at it, it looks up and glares at you..")
    print("\nWhat do you do?")
    print("1. Glare Back")
    print("2. Wave")
    print("3. Ignore it")
    print("=== use the number of the choice to answer ===")
    choice=input("> ")
    if(choice=="1"):
        print("\nYou glare back. It glares at you.\n...Nothing happens.")
        skeleton_helpful=False
    elif(choice=="2"):
        print("\nYou wave!\nShockingly it waves back, accidentally fumbling its book.\nIt mutters angrily as it shuffles away.")
        skeleton_helpful=True
    elif(choice=="3"):
        print("\nYou ignore it and go about your business.\nThe skeleton sighs dramatically, continuing to read.")
        skeleton_helpful=False
    else:
        print("\nWrong choice!\nThe skeleton throws a bone at you.")
        print("** damage taken **")
        health-=1
        skeleton_helpful=False
    print("\n** YOUR ACTIONS WILL HAVE CONSEQUENCES **")

#-----------------------------------
#DECIDING BEGINNING PATHWAY FUNCTION
def next_choice():
    print("\nAnyways...")
    print("Grabbing your fire lit torch you look around..\nUp ahead you see a sign pointing EAST to an armory and a blood stained hallway towards the WEST.")
    print("Where do you plan to go next?")
    print("1. EAST\n2. WEST")
    choice=input("> ")
    if(choice=="1"):
        print("You start heading towards the armory..")
        armory()
    elif(choice=="2"):
        print("You start heading towards the hallway..watch your step theres blood on the floor")
        hallway()
    else:
        print("Invalid choice! You wander aimlessly..forever, pick the right direction!")
        next_choice()
 
#------------------
#ARMORY PATH CHOSEN
def armory():
    global attack, has_iron_sword
    print("\nYou enter the RUSTY ARMORY. Dusty weapons line the walls.")
    print("You find a sturdy Iron Sword.")
    print("\n** IRON SWORD ADDED TO INVENTORY **")
    has_iron_sword=True
    attack+=3
    print("Your attack has increased\nAttack: ", attack)
    print("Suddenly you hear rustling...")
    fight_goblin()
    print("Oh hey you survived. Thats nice.")
    next_path_choice()
 
#-------------------
#HALLWAY PATH CHOSEN
def hallway():
    global attack, has_steel_sword
    print("\nGrimacing as you walk through the HALL, you jump as you find a rotten corpse.")
    print("Seeing as he held a sword and was currently dead so had no use for it..you grab it.")
    print("\n** STEEL SWORD ADDED TO INVENTORY **")
    has_steel_sword=True
    attack+=5
    print("Your attack has increased\nAttack: ", attack)
    print("\nUp ahead you hear a faint growl...")
    fight_goblin()
    print("\nOh hey you survived. Thats nice.")
    print("You notice an exit to the hallway up ahead...\nDo you stay and look around the hallway or head towards the exit?")
    print("1. Look Around\n2. Exit")
    path=input("> ")
    if path=="1":
        print("\nYou notice a small crack in the wall. Do you wish to investigate?\n1. Yes\n2. No")
        choice=input("> ")
        if choice=="1":
            secret_room()
        else:
            print("You decide to head towards the exit.")
            next_path_choice()
    else:
        next_path_choice()

#---------------------
#GOBLIN FIGHT FUNCTION
def fight_goblin():
    global health
    goblin_health=20
    goblin_attack=3
    fought = False
    print("\nA GOBLIN jumps out. Prepare yourself for a fight.")
    
    while goblin_health>0 and health>0:
        print("\nYour Health: ",health)
        print("Goblins Health: ", goblin_health)
        print("Do you \n1. Attack\n2. Run")
        action=input("> ")
        
        if action=="1":
            fought = True
            goblin_health-=attack
            print("\nYou slash at the goblin!\nGoblins Health: ", goblin_health)
            if goblin_health<=0:
                print("You defeated it...")
                break
            health-=goblin_attack
            print("\nThe goblin attacks you! Damage taken!\nHealth: ", health)
        elif action=="2":
            print("You run past the goblin..barely escaping harm.")
            break
        else:
            fought = True
            print("Wrong choices will get you killed.\nThe Goblin scratches you lightly. ")
            health-=1
            print("Health: ",health)
    if fought:    
        print("\nTired..you patch youself up a little.")
        health+=2
        print("** 2 HP Restored **")
        print("Health:", health)
    
    if health<=0:
        print("Ouch I think you just died.")
        print("** GAME OVER **")
        exit()

#--------------------------
#SECRET ROOM FOUND FUNCTION
def secret_room():
    global attack, has_diamond_sword
    print("\nYou squeeze through the crack, discovering a HIDDEN ROOM.")
    print("Torches flicker along the walls, casting long, dancing shadows.")
    print("At the center of the room, a diamond sword is perched on a pedestal.")
    print("\nSuddenly, a cold chill washes over you...")
    print("\nA pale vampire steps forward, his eyes gleaming in the torchlight.")
    print("\nDo you.. \n1. Approach the sword\n2. Step back\n3. Prepare to attack")
    choice = input("> ")
    if choice=="1":
        print("\nYou cautiously approach the sword. The vampire watches silently, a shadow flickering across his face.")
        print("As your hand hovers over the hilt, a whisper fills your mind...")
        print("\"Many have tried..all have failed..\"")
        print("Do you risk grabbing the sword?\n1.Yes\n2.No")
        grab=input("> ")
        if grab=="1":
            has_diamond_sword=True
            attack+=8
            print("\nYour fingers close around the hilt of the diamond sword. A cold shiver runs through you.")
            print("The vampire steps back, his eyes narrowing.\"So be it. But know, this sword carries a shadow of my curse.\"")
        else:
            print("You decide against taking the sword. The vampires shadowy form watches you silently before fading back into the darkness.")
    elif choice=="2":
        print("\nYou take a cautious step back. The vampire tilts his head, seeming almost amused.")
        print("\"Caution...perhaps wise.\"")
    elif choice=="3":
        print("\nYou prepare to fight!")
        print("\"I have better things to do than to fight you child. Leave.\"")
        print("\nYou quickly step back.")
    else:
        print("\nHesitation hangs in the air. The vampire studies you before retreating into the shadows.")
    print("\n** Slipping out through the crack **")
    next_path_choice()
    
#----------------------------
#NEXT PATHWAY CHOICE FUNCTION
def next_path_choice():
    print("\nAs you keep walking you come across a fork in your path.")
    print("Which way do you wish to go?")
    print("1. Left\n2. Right")
    choice=input("> ")
    if choice=="1":
        bone_pit()
    elif choice=="2":
        spider_nest()
    else:
        print("Wrong way..you bump into a wall. Think before you walk...")
        next_path_choice()

#-----------------
#BONE PIT FUNCTION
def bone_pit():
    global health, has_lockpick
    print("\nShuffling through the dark you come across a BONE PIT.")
    print("\nBones crunch under your feet.")
    if skeleton_helpful:
        print("Suddenly the skeleton from before appears and points out a safer path through the pit.")
        print("** YOU AVOIDED TRAPS **")
    else:
        print("Carelessly stepping over them, you trigger a trap.")
        print("\n** DAMAGE TAKEN **")
        health-=2
        print("Health: ",health)
        print("\nSpotting the skeleton from before, you watch its bones rattle as it laughs at you.")
    print("\nAs you keep walking you notice a shiny lockpick on the floor. You pick it up.")
    has_lockpick=True
    print("\n** LOCK PICK ADDED TO INVENTORY **")
    alchemy_room()
    
#---------------------
#SPIDER NEST FUNCTION
def spider_nest():
    global health, has_key
    print("\nShuffling through the dark you realise youve walked into a SPIDERS NEST.")
    print("Raising your torch, you spot a giant spider.")
    print("Surprisingly, the spider speaks..\n\"Greetings Traveller. Do you wish to answer my riddle?\"")
    print("1.Yes\n2.No")
    choice=input("> ")
    if choice=="1":
        print("\"Wonderful! Bill The Skeleton doesnt really talk, he more so just judges so its nice to have someone who can reply.")
        print("Answer the riddle Traveller. I speak without a mouth and hear without ears. What am I?\"")
        answer=input("> ").lower()
        if "echo" in answer:
            print("\"Correct! As a reward some advice, the ALCHEMY ROOM holds a key. Goodluck now!\"")
            has_key=True
        else:
            print("\"Wrong. Thats too bad. Off you go traveller, Im due for book club, Bill doesnt like to wait.\"")
    else:
        print("\"Thats too bad. Off you go traveller, Im due for book club, Bill The Skeleton doesnt like to wait.\"")
    alchemy_room()
    
#---------------------
#ALCHEMY ROOM FUNCTION
def alchemy_room():
    global has_potion
    print("\n** TIME SKIP **")
    print("You reach the ALCHEMY ROOM. Even though no one seems to be present, bottles bubble and smoke.")
    if has_key:
       print("\nYou search the room, finding a key on a shelf. This will aid your escape.")
       print("** KEY ADDED TO INVENTORY **")
    else:
        print("\nYou search the room but find nothing useful.")
        print("** PAST CHOICES HAVE AFFECTED YOUR SEARCH **")
    print("\nAs you walk towards a door you spot a sign pointing towards the exit of the dungeon.")
    print("As you go to leave you spot a glowing bottle filled with a neon coloured liquid.\n\nPicking it up, do you..")
    print("1. Drink it\n2. Leave it")
    choice=input("> ")
    if choice=="1":
        print("\nYour hair turns bright neon..it seems to be lighting up your path...")
        print("You put out your torch and continue towards the exit with giddy steps.")
        has_potion=True
    else:
        print("\nLeaving it, you continue towards the exit.")
    final_boss()

#-------------------
#FINAL BOSS FUNCTION
def final_boss():

    global health
    beast_health=40
    beast_attack=6

    print("\nExcited on finally knowing a way out you dont notice the sudden drop in temperature.")
    print("A giant beast emerges from the shadows, the wind picks up and wisps of shadows incompass your surroundings.")
    print("The beast lets out an ear shattering roar, the walls of the dungeon rattling.")

    print("\n** FINAL BATTLE HAS BEGUN **")
    print("\nBefore the beast strikes, you steady yourself.")
    print("== 5 HP regained ==")
    health+=5
    
    if has_potion:
        print("Suddenly the potion inside you glows brightly!")
        print("== potion restores 10 HP ==")
        health+=10
        
    while beast_health>0 and health>0:
        print("\n** Your Stats **")
        print("Health: ", health)
        print("Attack: ", attack)

        print("** Shadow Beasts Stats **")
        print("Health: ", beast_health)
        print("Attack: ", beast_attack)

        print("\n1.Attack\n2.Defend")
        action=input("> ")
        if action=="1":
            import random
            print("\nYou attack!")
            beast_health-=attack
            if random.random()<0.3:
                print("You dodge the Beasts attack!\nNo damage taken!")
            else:
                print("\nThe beast strikes!")
                health-=beast_attack
            if beast_health<=0:
                print("** BEAST DEFEATED **")
                break
        elif action=="2":
            print("\nYou defend!")
            reduced=beast_attack//3
            health-=reduced
            counter=attack//2
            beast_health-=counter
            print("You took reduced damage:",reduced)
            print("But countered with an attack of ", counter)
            if beast_health<=0:
                print("** BEAST DEFEATED **")
                break
        else:
            print("\nHesitation Traveller! It will get you killed..")
            print("The beast attacks you with full force!")
            health-=beast_attack

    if health<=0:
        print("\nYour strength falters..the beast towers over you.")
        print("As your final sparks of hope fade, so do you..")
        print("\nThe dungeon grows silent once more\nA nameless traveler lost to its shadows.")
        print("\nYou didnot survive this quest traveller i truly hoped you would have.")
        print("\n** QUEST FAILED **")
        print("==== ending : extinguished by darkness ====")
        print("** GAME OVER **")
        
        exit()
    exit_door()
    
#-------------------
#EXIT ROUTE FUNCTION
def exit_door():
    print("After defeating the Shadow Beast, you reach a massive door.")

    if has_key or has_lockpick:
        print("\nYou notice the door has a complex lock.")
        if has_key:
            print("Do you wish to try the key you found?\n1.Yes\n2.No")
            choice=input("> ")
            if choice=="1":
                print("Click! The door swings open..")
                print("\n** QUEST COMPLETED : YOU ESCAPED **")
                print("==== good ending achieved ====") #ending 1
                exit()
            else:
                print("You step back from the door, thinking about other options.")

        if has_lockpick:
            print("Do you wish to try using the lockpick you found?\n1.Yes\n2.No")
            choice=input("> ")
            if choice=="1":
                print("\nYou carefully work...")
                print("Click! The door swings open..")
                print("\n** QUEST COMPLETED : YOU ESCAPED **")
                print("==== good ending achieved ====") #ending 2
                exit()
            else:
                print("You step back from the door, thinking about other options.")

    if has_diamond_sword and health>10:
        print("\nYou feel your Diamond Sword pulse with energy...")
        print("Do you wish to attempt smashing the door?\n1.Yes\n2.No")
        choice=input("> ")
        if choice=="1":
            import random
            success=random.choice([True,False])
            if success:
                print("With all the strength you have left, you smash the door wide open!")
                print("\n** QUEST COMPLETED : YOU ESCAPED **")
                print("==== alternate ending achieved : escape through strength ====") #ending 3
                exit()
            else:
                print("\nThe door holds firm. The impact leaves you exhausted...")
                print("Darkness surrounds you as the dungeon swallows your hopes to escape...")
                print("Goodbye Traveler...I truly did hope your ending was better.")
                print("\n** QUEST FAILED **")
                print("==== bad ending achieved ====") #ending 4
                exit()

    print("\nWithout any means to open the door, you remain trapped...")
    print("Darkness surrounds you as the dungeon swallows your hopes to escape...")
    print("Goodbye Traveler...I truly did hope your ending was better.")
    print("\n** QUEST FAILED **")
    print("==== bad ending achieved ====")
    exit()

#start the game
main_menu()