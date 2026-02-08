import time
import os
def print_menu():
    options = [1, 2]
    option = 0
    while(option not in options):
        print_options()
        option = int(input("Option: "))

            

def print_options():
    print("Hello! Please select an option.")
    print("1. Guess the number")
    print("2. Calculator")

def manage_option(option):
    if (option == 1):
        pass
    if (option == 2):
        pass