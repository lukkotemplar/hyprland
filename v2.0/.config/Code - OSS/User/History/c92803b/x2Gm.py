def print_menu():
    option = 0
    while(option == 0):
        print("Hello! Please select an option.")
        print("1. Guess the number")
        print("2. Calculator")
        option = input("Option: ")
        if (option != 1 and option != 2):
            option = 0
            print("Please select a valid option")



