from menu import *

if __name__ == '__main__':
    while True:
        try:
            show_menu()
        except ValueError:
            print("Invalid input, please enter a number corresponding to the menu options")