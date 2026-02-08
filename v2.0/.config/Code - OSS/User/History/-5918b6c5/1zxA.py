import time
import os
import random
import math
from pda import print_menu
def init():
    os.system('clear')
    game()

def game():
    attempts = 0
    print("Hello! Try to guess my number, you have three attempts")
    while attempts < 3:
        hidden_no = random.randint(1,50)
        guess = int(input("Number: "))
        if (guess != hidden_no):
            print("Wrong number!")
            attempts = attempts + 1
        else:
            print("Correct!!")
            retry = input("You wanna keep playing? (Y/N)")
            if (retry == "yes"):
                attempts = 0
            else:
                print_menu()
