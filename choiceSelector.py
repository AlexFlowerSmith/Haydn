from os import system, name
import sys, time, random

# creates a clear screen function
def clear():
    input() # empty input intended to slow down speed of program usage / prevent personal overloading
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')


# creates a slowprint function
def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.06)


# creates a fastprint function
def fastprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.010)


# pre-menu screen + user selection mechanism
def selector():
    """basic pre-menu fun"""
    choice = input("Press any key to start")
    if choice == '1':  # Secret option to skip ahead to playGame()
        playGame()
    clear()
    fastprint("+-+-+-+-+-+-+-+-")
    slowprint(" Haydn's Very Good Selection Program ")
    fastprint("+-+-+-+-+-+-+-+-\n")
    fastprint("This program will help you decide what the fuck to do! :)\n")
    menuScreen() # main menu screen recalled without animated print


def playGame():
    secretOption = "Mine Sweeper\nHA HA HA BIG BEAN"

    choices = input("How many options do you have?\n> ")
    choices = int(choices)       # typecast choices from str to int
    choice_list = [secretOption] # initialise list with secretOption already included
    for i in range(1, choices + 1): # ensure starting index is 1
        choice = input(f"Name of number {i} choice: ")
        choice_list.append(choice)
    slowprint("The anwser is......\n")
    answer = random.choice(choice_list)
    #decider(choices, choice_list, answer, secretOption) < old testing function
    if answer != secretOption:
        input()
        print(answer)
        menuScreen()
    else:
        input()
        print("ERROR. HA HA BIG BEAN YOU FUCKED IT UP.\n")
        fastprint("!!!!!!!!!!!!!@@@@@@@@@@@@@!!!!!!!!!!!!!!!!\n")
        print(f"You MUST choose {secretOption} :)\n")
        clear()
        menuScreen()


def menuScreen():
    """Display menu with print, not fast/slow print, and call menuScreenSelector() for input"""
    clear()
    print("+-+-+-+-+-+-+-+- Haydn's Very Good Selection Program +-+-+-+-+-+-+-+-\n")
    fastprint("1. Play  2. Patch Notes  3.  Quit\n")
    menuScreenSelector()


def menuScreenSelector():
    """ Menu screen input handling function"""
    menu_choice = input("> ")
    if menu_choice == '1':
        playGame()
    elif menu_choice == '2':
        patchNotes()
    else:
        quit()


def patchNotes():
    """Disply patch notes and option to return to menu"""
    clear()
    print("+-+-+-+-+-+-+-+-+-+- Patch Notes from a Dumb Dev +-+-+-+-+-+-+-+-+-+-\n")
    fastprint("ATTENTION\nWow, 16th September '23 was V1? That's wild.\n")
    fastprint("Now I'm making a V2 at friggin 0530 in the morning lol\n")
    input("\nENTER to return to menu")
    menuScreen()

''' Old testing function
def decider(choices, choice_list, answer, secretOption):
    # Testing outputs, choices + length of list + answer
    print(f"The number of choices: {choices}")
    print(len(choice_list))
    print(answer)
''' 
    
selector()
