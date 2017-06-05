"""
Password Generator. The program will do the following:
1. Prompt user for a desired password length.
2. Generate a random string of letters, numbers, and punctuation.
3. Print out the generated string as the password.
"""

import random
from time import sleep

# Takes user input for length of password - generates random password


def generator():
    menu_on = True
    while menu_on is True:
        pw_length = int(raw_input("Enter how many characters you would like the password to contain (max - 35 char.): "))
        chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        if pw_length <= 35:
            pw_generation = random.sample(chars, pw_length)
            new_pw = "".join(pw_generation)
            print "Your new password is: %s" % (new_pw)
            menu_on = False
        elif pw_length > 35:
            print "Error - You've entered an invalid input value"

# Manages game menus - allows user to start new game or exit


def game_menu():
    game_on = True
    print "Welcome to Password Generator! You'll find your main menu below:"
    while game_on is True:
        menu = raw_input("\nMain Menu\nEnter 'N' to create a new password\nEnter 'X' to exit\nEnter your input here: ")
        if menu == "N" or menu == "n":
            print "\nOpening..."
            sleep(1)
            generator()
            sleep(1)
            menu2_on = True
            while menu2_on is True:
                menu_2 = raw_input("Would you like to try again? Enter 'Y' to generate a new password - Enter 'N' to exit: ")
                if menu_2 == "Y" or menu_2 == "y":
                    menu2_on = False
                elif menu_2 == "N" or menu_2 == "n":
                    menu2_on = False
                    game_on = False
                else:
                    print "Error - You've entered an invalid input value"
                    menu2_on = True
        elif menu == "X" or menu == "x":
            game_on = False
        else:
            print "\nError - You've entered an invalid input value"
            game_on = True


game_menu()
