import time
import os
def print_menu():
    option = 0
    while(option == 0):
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