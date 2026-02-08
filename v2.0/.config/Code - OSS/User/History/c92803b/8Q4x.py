import time
import os
import guessing
def print_menu():
    options = [1, 2]
    option = 0
    while(option not in options):
        print_options()
        option = int(input("Option: "))
        manage_option(option)
            

def print_options():
    print("Hello! Please select an option.")
    print("1. Guess the number")
    print("2. Calculator")

def manage_option(option):
    if (option == 1):
        guessing.init()
    if (option == 2):
        pass