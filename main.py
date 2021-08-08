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
|     V2.0      |
=================''')
time.sleep(2)
clear()
v = '2.0'
vint = int(2)
def mainrun():
    def set_players():
        clear()
        set_p = True
        print("Exit code is !x")
        while set_p:
            input_name = input("Name: ")
            if input_name == "!x":
                set_p = False
                menu()
            playerls.append(input_name)
    def config_wiz():
        clear()
        print("Welcome to the Config Wizard.\nPlease select from one of the following options:\n1) Load Config\n2) Create config from current settings\n3) Create new config\n4) Exit config")
        config_command = ()
        while config_command not in range(1,5):
            config_command = int(input("DnD> "))
        if config_command == 1:
            print("To allow the tool to find and load the config, move to config text file into the same directory as this tool. Then, enter the name of the file - without the .dndtoolconf.txt extention.")
            file_name = input("configwiz> ")
            print("Searching...")
            try:
                config_file = open(f"./{file_name}.dndtoolconf.txt")
                print("Reading...")
                config_conts = config_file.read()
                config_file.close()
                config_conts = config_conts.replace("=", "\n")
                config_ls = config_conts.split("\n")
                config_ls.pop(0)
                wplayersls = config_ls[5].split("~")
                print("Players located!")

                versionconf = config_ls[1].split(".")
                print(versionconf)
                input()
                if versionconf[0] == "β":
                    print("!Warning! This config was generated by a beta version of this tool - some features may not work.")
                    nversionconf = int(versionconf[1])
                else:
                    nversionconf = int(versionconf[0])
                if nversionconf > vint:
                    print("!Warning! This config was made by a newer version of this tool than the one you are running. It is reccomended that you update your tool to avoid issues.")
                if nversionconf < vint:
                    print("!Warning! This config was made by an older version of this tool than the one you are running, some features may not work. It is reccomended that you regenerate the config to avoid issues.")
                for x in range(len(wplayersls)):
                    print(wplayersls[x])
                confirm = ''
                while confirm not in ('y', 'Y', 'n', 'N'):
                    confirm = input("Is that correct (y/n)? ")
                if confirm in ('y', 'Y'):
                    for x in range(len(wplayersls)):
                        playerls.append(wplayersls[x])
                else:
                    clear()
                    menu()
            except:
                input("Something went wrong...")
                menu()
        if config_command == 2:
            filename = input("What should we call the file? ")
            groupname = input("And what is the name of the group? ")
            configfile = open(f"./{filename}.dndtoolconf.txt", "w")
            joinchar = "~"
            playerstring = joinchar.join(playerls)
            configfile.write(f'''!! This is a config file generated by DnD Dice Tools. To use, move to the same directory as the tool file then navigate to the Config Wizard and select option 1
v={v}
name={groupname}
players={playerstring}''')
            configfile.close()
            input("File made!")
            menu()
        if config_command == 3:
            tplayerls = []
            filename = input("What should we call the file? ")
            groupname = input("And what is the name of the group? ")
            configfile = open(f"./{filename}.dndtoolconf.txt", "w")
            joinchar = "~"
            set_p = True
            print("Enter the names of the players\nThe exit code is !x")
            while set_p:
                input_name = input("Name: ")
                if input_name == "!x":
                    set_p = False
                    break
                tplayerls.append(input_name)
            playerstring = joinchar.join(tplayerls)
            configfile.write(f'''!! This is a config file generated by DnD Dice Tools. To use, move to the same directory as the tool file then navigate to the Config Wizard and select option 1
v={v}
name={groupname}
players={playerstring}''')
            configfile.close()
            input("File made!")
            menu()
        if config_command == 4:
            clear()
            menu()
    def menu():
        if len(playerls) == 0:
            print("!! No players have been added yet. Please run option run before rolling any group dice to avoid errors. !!")
        print("DnD Dice Tool\nPlease select from one of the following options:\n1) Set players\n2) Run D20 for all\n3) Run D20 for one\n4) Run Dx for all\n5) Run Dx for one\n6) Print players\n7) Clear terminal\n8) Config Wizard\n9) About\n0) Exit")
        menu_option = ()
        while menu_option not in range(1,10):
            menu_option = int(input("DnD> "))
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
            menu()
        if menu_option == 8:
            clear()
            config_wiz()
            menu()
        if menu_option == 9:
            print(f'''
*=======================================================*
| DnDTool by James King                                 |
| Version {v}                                           |
| Provided under the MIT licence, distributed on GitHub |
| www.JamesDev.co.gg                                    |
*=======================================================*
''')
            input()
            clear()
            menu()
        if menu_option == 0:
            exit()

    menu()

mainrun()