from os import system, name
import sys, time, random

# creates a clear screen function
def clear():
    input()
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


# menu screen + user selection mechanism
def selector():
 
    input("Press any key to start")
    clear()
    fastprint("+-+-+-+-+-+-+-+-")
    slowprint("   Haydn's Very Good Selection Program ")
    fastprint("+-+-+-+-+-+-+-+-\n")
    fastprint("This program will help you decide what the fuck to do! :)\n")
    slowprint("ATTENTION\nThis program is a first version demo, so give three options every time!\n")
    slowprint("Eventually I'll figure out the logic for x amount of choices\n")
    choices = str(input("How many options do you have?\n> "))
    optionOne = str(input("First Option:\n> "))
    optionTwo = str(input("Second Option:\n> "))
    optionThree = str(input("Third Option:\n> "))
    secretOption = "Mine Sweeper\n HA HA HA BIG BEAN "
    tehArray = [optionOne, optionTwo, optionThree, secretOption]
    tehAnswer = random.choice(tehArray)

    if tehAnswer == optionOne:
        tehAnswer = optionOne
    elif tehAnswer == optionTwo:
        tehAnswer = optionTwo
    elif tehAnswer == optionThree:
        tehAnswer = optionThree
    elif tehAnswer == secretOption:
        tehAnswer = secretOption
    else:
        print("ERROR. HA HA BIG BEAN YOU FUCKED IT UP.\n")
        fastprint("!!!!!!!!!!!!!@@@@@@@@@@@@@!!!!!!!!!!!!!!!!")

    fastprint("Thinking.................\n")
    fastprint("Checking if you are on the FBI most wanted\n")
    fastprint("Checking the CIA records, too\n")
    fastprint("Checking Domingo's Friends List\n")
    fastprint("Deciding if I want a Zambrero burrito or GYG\n")
    fastprint("Yeah maybe not, I gotta be better\n")
    fastprint("LOADING ANSWER...........")
    fastprint("IT'S CUMMING..........")
    clear()
    print(tehAnswer + " :)\n")




selector()
