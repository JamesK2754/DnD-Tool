import random
import time
import os

playerls = []
clear = lambda: os.system('clear')

print('''
=================
| DnD Dice Tool |
| by James King |
|  MIT Licence  |
|     V1.0      |
=================''')
time.sleep(2)
clear()
def mainrun():
    def set_players():
        set_p = True
        print("Exit code is !x")
        while set_p:
            input_name = input("Name: ")
            if input_name == "!x":
                set_p = False
                menu()
            playerls.append(input_name)

    def menu():
        if len(playerls) == 0:
            print("!! No players have been added yet. Please run option run before rolling any group dice to avoid errors. !!")
        print("DnD Dice Tool\nPlease select from one of the following options:\n1) Set players\n2) Run D20 for all\n3) Run D20 for one\n4) Run Dx for all\n5) Run Dx for one\n6) Print players\n7) Clear terminal\n8) Exit")
        menu_option = ()
        while menu_option not in [1,2,3,4,5,6,7,8]:
            menu_option = int(input())
        if menu_option == 1:
            set_players()
        if menu_option == 2:
            for x in range(len(playerls)):
                num = random.randint(1,20)
                print(f"{playerls[x]} {num}")
            input()
            menu()
        if menu_option == 3:
            print(random.randint(1,20))
            input()
            menu()
        if menu_option == 4:
            d = int(input("roll a d"))
            for x in range(len(playerls)):
                num = random.randint(1,d)
                print(f"{playerls[x]} {num}")
            input()
            menu()
        if menu_option == 5:
            d = int(input("roll a d"))
            print(random.randint(1, d))
            input()
            menu()
        if menu_option == 6:
            if len(playerls) > 0:
                print("players are...")
                for x in range(len(playerls)):
                    print(playerls[x])
            else:
                print("No players were found in list.")
            input()
            menu()
        if menu_option == 7:
            clear()
            print("cleared")
            menu()
        if menu_option == 8:
            exit()

    menu()

mainrun()
