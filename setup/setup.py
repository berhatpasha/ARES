import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
import time

Os = None #
loader = None #
user = None #
version = "0.0.1" #
recoveryMode = "false" #
err = None

if os.name == 'posix':
    Os = "unix"
    os.system('clear')
elif os.name == 'nt':
    Os = "win"
    os.system('cls')
else:
    os.system('clear')

def intro():
    if Os == "win":
        os.system('cls')
    else:
        os.system('clear')
    print('''PLEASE WAİT''')


while True:
    try:
    
        print(f"{Fore.CYAN}Please enter installation information")
        # loader 
        while True:
            print(f'''{Fore.LIGHTBLUE_EX}[1]{Fore.LIGHTGREEN_EX}MSI {Fore.LIGHTBLUE_EX}[2]{Fore.LIGHTGREEN_EX}GIGABYTE {Fore.LIGHTBLUE_EX}[3]{Fore.LIGHTGREEN_EX}LENOVO {Fore.LIGHTBLUE_EX}[4]{Fore.LIGHTGREEN_EX}ASUS
{Fore.LIGHTBLUE_EX}[5]{Fore.LIGHTGREEN_EX}Biostar {Fore.LIGHTBLUE_EX}[6]{Fore.LIGHTGREEN_EX}ZOTAC {Fore.LIGHTBLUE_EX}[7]{Fore.LIGHTGREEN_EX}ASRock {Fore.LIGHTBLUE_EX}[8]{Fore.LIGHTGREEN_EX}NZXT''')
            Input = input(f"{Fore.LIGHTCYAN_EX}select>>{Fore.BLUE}")
            if Input.split()[0] == "1":
                loader = "msi"
                break
            elif Input.split()[0] == "2":
                loader = "gigabyte"
                break
            elif Input.split()[0] == "3":
                loader = "lenovo"
                break
            elif Input.split()[0] == "4":
                loader = "asus"
                break
            elif Input.split()[0] == "5":
                loader = "biostar"
                break
            elif Input.split()[0] == "6":
                loader = "zotac"
                break
            elif Input.split()[0] == "7":
                loader = "asrock"
                break
            elif Input.split()[0] == "8":
                loader = "nzxt"
                break
            else:
                print(f"{Fore.LIGHTYELLOW_EX}invalid")
    
        # OS
        if Os == "win":
            while True:
                print(f'''{Fore.LIGHTBLUE_EX}[1]{Fore.LIGHTGREEN_EX}Windows{Fore.BLUE}(detected) {Fore.LIGHTBLUE_EX}[2]{Fore.LIGHTGREEN_EX}Unix''')
                Input = input(f"{Fore.LIGHTCYAN_EX}select>>{Fore.BLUE}")
                if Input.split()[0] == "1":
                    Os = "win"
                    Input = input(f"{Fore.MAGENTA}open recovery mode when disk is inserted? (recommended:Y) (Y/n)")
                    if Input.split()[0].lower() == "y":
                        recoveryMode=="true"
                    else:
                        recoveryMode=="false"
                    break
                elif Input.split()[0] == "2":
                    Os = "unix"
                    break
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}invalid")
        elif Os == "unix":    
            while True:
                print(f'''{Fore.LIGHTBLUE_EX}[1]{Fore.LIGHTGREEN_EX}Windows {Fore.LIGHTBLUE_EX}[2]{Fore.LIGHTGREEN_EX}Unix{Fore.BLUE}(detected)''')
                Input = input(f"{Fore.LIGHTCYAN_EX}select>>{Fore.BLUE}")
                if Input.split()[0] == "1":
                    Os = "win"
                    Input = input(f"{Fore.MAGENTA}open recovery mode when disk is inserted? (recommended:Y) (Y/n)")
                    if Input.split()[0].lower() == "y":
                        recoveryMode=="true"
                    else:
                        recoveryMode=="false"
                    break
                elif Input.split()[0] == "2":
                    Os = "unix"
                    break
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}invalid") 
                    
        while True:
            print(f'''{Fore.LIGHTBLUE_EX}[1]{Fore.LIGHTGREEN_EX}only for this user {Fore.LIGHTBLUE_EX}[2]{Fore.LIGHTGREEN_EX}for All users (default)''')
            Input = input(f"{Fore.LIGHTCYAN_EX}select>>{Fore.BLUE}")    
            if Input.split()[0] == "1":
                user = input(f"{Fore.LIGHTCYAN_EX}username>>{Fore.BLUE}") 
                break
            elif Input.split()[0] == "2":
                user = None
                break
            else:
                print(f"{Fore.LIGHTYELLOW_EX}invalid")
            
    except:
        print("passed")
        err = 1
    if err == 1:
        pass
    else:
        break