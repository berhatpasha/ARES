import time
import colorama
from colorama import Fore
import os
colorama.init(autoreset=True)

os.system("cls")

def one():
    pass

def two():
    pass

def three():
    pass

print("\n")
print(f"{Fore.CYAN} Service launched ! ")
time.sleep(3)
print("\n")
print(f"{Fore.LIGHTCYAN_EX} Select one of them : ")
print(f"{Fore.LIGHTCYAN_EX} [1] System restore")
print(f"{Fore.LIGHTCYAN_EX} [2] scan for viruses and threats")
print(f"{Fore.LIGHTCYAN_EX} [3] clean viruses and threats (6)")
while True:
    Input=input(f" {Fore.LIGHTMAGENTA_EX}-$ {Fore.WHITE}")
    
    match Input.split()[0]:
        case "1":
            one()
        case "2":
            two()
        case "3":
            three()
        case _:
            print(f" {Fore.LIGHTYELLOW_EX} Please enter an existing option directly (e.g. 1)")
