from os import system
from random import randint

gametitle = "Castle Dungeons - an interactive story game"
system("mode 110,30")
system("title" + gametitle)



def cls():
    system('cls')


character_name = None
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None

cls()
print("Castle Dungeons - An interactive fiction game in Python.")


def Intro():
    print("")
    print("In this adventure, you are the hero.")
    print("Your choices, skills and a bit of luck, will influencce the outcome of the game")
    print("")
    print("An evil sorcerer is holding your felloe adventurers prisoner.")
    print("Will you succeed to free your friends from the castle dungeons, or peril trying")
    print("")
    input("Press Enter to start...")


Intro()


def create_character():
    cls()
    global character_name
    character_name = input("""
		Lets begin by creating your character.
		What is your character name?

		>""")
    global character_race
    while character_race is None:
        race_choice = input("""
		Choose your character race from the list below by entering the relevant number
			1 - Elf
			2 - Dwarf

			> """)
        if race_choice == "1":
            character_race = "Elf"
        elif race_choice == "2":
            character_race = "Dwarf"
        else:
            print("Not a valid choice, try again")
    cls()
    global character_class
    while character_class is None:
        class_choice = input("""
		Choose your characterc class from the list below by entering the relevant number
			1  - Warrior 
			2  - Wizard

			> """)
        if class_choice == "1":
            character_class = "Warrior"
        elif class_choice == "2":
            character_class = "Wizard"
        else:
            print("Not a valid choice, try again")


create_character()


def create_character_skill_sheet():
    cls()
    global character_name, character_class, character_race, character_strength, character_dexterity, character_magic, character_life
    print("""
	Now let's determine the character skills using random library(call it lucg):
	we have four skills 

	- Strength :desc
	- Dexterity : desc
	- Magic:desc
	- Life:desc



	Depending on your race and class you will hae certain point base already calculated
	You will shortly be bale to increase your skill using a 6 faced die.

	Here is your base Character Skills Sheet:
	""")
    character_strength = 5
    character_magic = 0
    character_dexterity = 3
    character_life = 10
    if character_race == "Elf":
        character_strength = character_strength + 3
        character_magic = character_magic + 6
        character_dexterity = character_dexterity + 4
        character_life = character_life + 2
    elif character_race == "Dwarf":
        character_strength = character_strength + 5
        character_life = character_life + 4
    if character_class == "Warrior":
        character_strength = character_strength + 3
        character_life = character_life + 3
    elif character_class == "Wizard":
        character_magic = character_magic + 4
    print("""
	Name:""" + character_name +
          """
          Race: """ + character_race +
          """
          Class: """ + character_class +
          """
      
          Strength: """ + str(character_strength) +
          """
          Dexterity:""" + str(character_dexterity) +
          """
          Magic:""" + str(character_magic) +
          """
          Life: """ + str(character_life) + """

	""")
    input("Preess Enter to apply your sills modifiers")


create_character_skill_sheet()


def modify_skills():
    cls()
    global character_strength, character_dexterity, character_life
    print("To modify your skills, roll a six faced die for skill change")
    input("Press Enter to roll for strength")
    roll = randint(1, 6)
    print("you rolled:: " + str(roll))
    character_strength = character_strength + roll
    input("Press Enter to roll for dexterity")
    roll = randint(1, 6)
    print("you rolled:: " + str(roll))
    character_dexterity = character_dexterity + roll
    input("Press Enter to roll for Life")
    roll = randint(1, 6)
    print("you rolled:: " + str(roll))
    character_life = character_life + roll
    input("Press enter to continur")
    cls()
    print("""
	Congratulations! You have completed your character creation, 
	Your final character sheet is:

	Name:""" + character_name +
          """
          Race: """ + character_race +
          """
          Class: """ + character_class +
          """
      
          Strength: """ + str(character_strength) +
          """
          Dexterity:""" + str(character_dexterity) +
          """
          Magic:""" + str(character_magic) +
          """
          Life: """ + str(character_life) + """

	""")
    input("Now go and begin your adventure!! PRESS ENTER")


modify_skills()


def Scene_1():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
		You hav entered the Castle Dungeons..
		It is dark however thankfully your torch is lit and your surroundings  are visible though barely.
		The stone walls are damp, the smell of rats and dungeon crawlers are everywhere!!, now ou begin walking down the corridoe
		and there is a turn . You have one of two choices




		What do you do?
		1- Turn left
		2- Turn right
		> """)
        if user_input == "1" or user_input == "turn left":
            choice = "1"
            Scene_2()
        elif user_input == "2" or user_input == "turn right":
            choice = "2"
            Scene_3()
        else:
            print("""
			The demons are coming, hurry make a realistic choice!!
			""")


def Scene_2():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
	From the darkness behind you.. you hear a strange noise..

	What do you do?

	1 - continue walking
	2 - stop to listen

	> """)
        if user_input == "1" or user_input == "continue":
            choice = "1"
            combat()
        elif user_input == "2" or user_input == "stop":
            choice = "2"
            skill_check()
        else:
            print("""
			The demons are coming, hurry make a realistic choice!!
			""")


def Scene_3():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
	From the darkness ahead of you.. you hear a strange noise..

	What do you do?

	1 - continue walking
	2 - stop to listen

	> """)
        if user_input == "1" or user_input == "continue":
            choice = "1"
            combat()
        elif user_input == "2" or user_input == "stop":
            choice = "2"
            skill_check()
        else:
            print("""
			The demons are coming, hurry make a realistic choice!!
			""")


def skill_check():
    cls()
    print("A giant rock falls on from the ceiling, roll a die or be ready to die")
    roll = randint(1, 6)
    print("You rolled:" + str(roll))
    if roll + character_dexterity > 10:
        print("""
			You dodged the stone and survived, danger is not over though
			The noise persists!!""")
        input("Press enter to continue")
        combat()
    else:
        print("You are dead your dexterity was not enough")
        input("Press enter to exit the game")


def combat():
    cls()
    global character_life
    print("A big smelly orc attacks you!")
    input("Press enter to combat")
    orc = [10, 14]  # stregth and life in order
    while orc[1] > 0 and character_life > 0:
        char_roll = randint(1, 6)
        print("You rolled:" + str(char_roll))
        monst_roll = randint(1, 6)
        print("The monster rolled:" + str(monst_roll))
        if char_roll + character_strength >= monst_roll + orc[0]:
            print("You hit the monster!")
            orc[1] = orc[1] - randint(1, 6)
        else:
            print("The mosnter hits you!")
            character_life = character_life - randint(1, 6)
    if character_life > 0:
        print("You defeated the orc, congratulations! You rescued tour friends!!")
        input("Press enter to exit the game")
    else:
        print("You lost, your friends will never be found!! ")
        input("Press enter to exit")


Scene_1()