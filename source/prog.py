import subprocess
import threading
import os 
import time
import colorama
from colorama import Fore
import keyboard
colorama.init(autoreset=True)

def secureMode():
    pass


#! critical
def backup():
    os.system('start kernel/backup.exe')
    #os.system('clear')
    print(f"{Fore.CYAN}TRANSACTION COMPLETED ! YOU CAN REMOVE THE DISK")
    if os=="windows":
        if rcMODE == True:
            os.system('bcdedit /set {default} safeboot minimal')
            os.system('shutdown /r /t 0')
            os.system(f'wmic logicaldisk where deviceid="{disk}" call dismount')
            
    else:
        pass
        subprocess.run('umount', f"/media/{username}/E", check=True)
        # Bu kısımlar üzerine çalış
    exit()
    


main = threading.Thread(target=backup)


disk = os.getcwd()[0]

if disk == "/" or disk == "C:":
    print(f"{Fore.RED}incorrect installation or false start err : 001")
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
    
with open('kernel/recoveryMode','r') as file:
    if file.read() == "auto" or file.read() == "true":
        rcMODE = True
    else:
        rcMODE = False
        
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

main.start()
main.join()
time.sleep(2)   
os.system(cleaner)
#   Banner
with open('kernel/time','r') as file:
    timeR = file.read()
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
██▓▓░░░░░░░░░░░░░░░░░░░░░░░░██  {Fore.GREEN}COMPLATED İN {timeR.split()[0]} MS{Fore.LIGHTYELLOW_EX}
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

time.sleep(5)
os.system(cleaner)

print(f'''{Fore.LIGHTGREEN_EX}
[1] Format  [2] Back to restore point [3] Exit
''')

def one():
    os.system('start kernel/one.exe')

def two():
    os.system('start kernel/two.exe')

def exitR():
    os.system(cleaner)
    print(f"{Fore.GREEN}transaction terminated")
    time.sleep(1)
    os.system(cleaner)
    print(f'''{Fore.LIGHTGREEN_EX}
ARES ARES       ARES ARES     ARES ARES   ARES ARES  {Fore.CYAN}{version}{Fore.LIGHTGREEN_EX}  
ARES  ARES      ARES   ARES   ARES       ARES        {Fore.CYAN}{Os}{Fore.LIGHTGREEN_EX}
ARES   ARES     ARES   ARES   ARES ARES    ARES      {Fore.CYAN}{loader}{Fore.LIGHTGREEN_EX}
ARES    ARES    ARES  ARES    ARES ARES       ARES   {Fore.CYAN}GNU LİCENSE{Fore.LIGHTGREEN_EX}
ARES     ARES   ARES   ARES   ARES             ARES  
ARES      ARES  ARES    ARES  ARES ARES  ARES ARES
''')
    time.sleep(2)

keyboard.on_press_key("1", lambda _: one())
keyboard.on_press_key("2", lambda _: two())
keyboard.on_press_key("3", lambda _: exitR())
keyboard.wait()