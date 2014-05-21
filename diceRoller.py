#dice roll program
#the purpose of this program is to roll a dice and present it to the user as if it was an actual dice using ASCII art.

import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"
x = 0
def roll():
    print("rolling...")
    roll = random.randint(1,6)
    return roll

    

def show_dice(roll):
    global x
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    else:
        print(s6)
        x = x + 10
    return myroll
    return x

User_Input = input("type 'roll' to roll the dice. ")
if User_Input == "roll":
    myroll = roll()
else:
    quit

    

time.sleep(1)

show_dice(myroll)
