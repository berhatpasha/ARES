import subprocess
import threading
import os 
import time
import colorama
import shutil
from colorama import Fore
colorama.init(autoreset=True)


def backup():
    os.system('./kernel/backup')
    print(f"{Fore.CYAN} TRANSACTION COMPLETED ! YOU CAN REMOVE THE DISK")


main = threading.Thread(target=backup)
main.start()


disk = os.getcwd()[0]

if disk == "/" or disk == "C:":
    print(f"{Fore.RED} incorrect installation or false start err : 001")
    time.sleep(3)
    #exit()

with open('kernel/os','r') as file:
    Os = file.read()

with open('kernel/version','r') as file:
    version = file.read()
    
with open('kernel/loader','r') as file:
    loader = file.read()

with open('kernel/database','r') as file:
    database = file.read()
    
with open('kernel/user','r') as file:
    username = file.read()

if Os == "windows":
    cleaner = "cls"
    os.system(cleaner)
    print(" "*10)
    print(f"{Fore.CYAN}configured according to {Fore.GREEN}windows")
else:
    cleaner = "clear"
    os.system(cleaner)
    print(" "*10)
    print(f"{Fore.CYAN}configured according to {Fore.GREEN}linux")

time.sleep(2)   
os.system(cleaner)
#   Banner
print(f'''{Fore.LIGHTYELLOW_EX}           
          ██████████       
          ██▒▒▒▒▒▒██          
          ██▓▓▒▒▓▓██          
          ██▓▓▓▓▓▓██            {Fore.CYAN}{loader}{Fore.LIGHTYELLOW_EX}
      ████▓▓██▓▓██░░████        {Fore.CYAN}{Os}{Fore.LIGHTYELLOW_EX}
    ██▓▓▓▓▓▓██████░░░░░░██      {Fore.CYAN}{version}{Fore.LIGHTYELLOW_EX}
  ██▓▓▓▓░░░░▓▓▓▓▓▓░░  ░░░░██    {Fore.CYAN}ARES RELEASE{Fore.LIGHTYELLOW_EX}
  ██▓▓░░░░░░░░░░░░░░░░  ░░██    {Fore.CYAN}C++ & Python based version{Fore.LIGHTYELLOW_EX}
██▓▓░░░░░░░░░░░░░░░░░░░░░░░░██  {Fore.CYAN}You can access the license on Github{Fore.LIGHTYELLOW_EX}
██▓▓░░░░░░░░░░░░░░░░░░░░░░░░██  {Fore.CYAN}The disk will be deactivated when the process is finished{Fore.LIGHTYELLOW_EX}
██▓▓░░██████░░░░░░██████░░░░██    
██▓▓██{Fore.LIGHTRED_EX}▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██░░██{Fore.LIGHTRED_EX}▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██░░██
██▓▓██{Fore.LIGHTRED_EX}▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██░░██{Fore.LIGHTRED_EX}▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██░░██
██▓▓██{Fore.LIGHTRED_EX}▓▓▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██{Fore.LIGHTRED_EX}▓▓▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██░░██
██▓▓░░████{Fore.LIGHTRED_EX}▓▓▓▓▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}████░░░░██
██▓▓▓▓░░░░██{Fore.LIGHTRED_EX}▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}██░░░░░░░░██
  ██▓▓░░░░██████████░░░░░░██  
    ██▓▓░░██      ██░░░░██    
      ██▓▓██      ██░░██      
        ████      ████
''')

time.sleep(3)
os.system(cleaner)

main.join()
print(f'''{Fore.LIGHTGREEN_EX}
[1] Format  [2] Back to restore point [3] Exit
''')
Input = input(f"{Fore.LIGHTBLUE_EX}Select one of them: {Fore.WHITE}")
if Input.split()[0].lower() == "1" and Input.split()[0].lower() == "one":
    pass
elif Input.split()[0].lower() == "1" and Input.split()[0].lower() == "two":
    pass
else:
    os.system(cleaner)
    print(f"{Fore.GREEN} transaction terminated")
    time.sleep(1)
    os.system(cleaner)
    print(f'''{Fore.LIGHTGREEN_EX}
ARES ARES       ARES ARES     ARES ARES   ARES ARES  {Fore.CYAN}{version}{Fore.LIGHTGREEN_EX}  
ARES  ARES      ARES   ARES   ARES       ARES        {Fore.CYAN}{Os}{Fore.LIGHTGREEN_EX}
ARES   ARES     ARES    ARES  ARES ARES    ARES      {Fore.CYAN}{loader}{Fore.LIGHTGREEN_EX}
ARES    ARES    ARES ARES     ARES ARES       ARES   {Fore.CYAN}GNU{Fore.LIGHTGREEN_EX}
ARES     ARES   ARES   ARES   ARES             ARES 
ARES      ARES  ARES    ARES  ARES ARES  ARES ARES
''')
    time.sleep(2)
    if os=="windows":
        pass
    else:
        pass
        subprocess.run('umount', f"/media/{username}/E", check=True)
    exit()
    