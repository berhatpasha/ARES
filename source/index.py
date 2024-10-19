import threading
import os 
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


with open('kernel/os','r') as file:
    Os = file.read()

with open('kernel/version','r') as file:
    version = file.read()
    
with open('kernel/loader','r') as file:
    loader = file.read()

with open('kernel/database','r') as file:
    database = file.read()

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
    
    
def main():
    time.sleep(2.5)
    print(f"{Fore.CYAN}recovery in progress: ")
    print(f"{Fore.GREEN}{len(database.split())} {Fore.LIGHTBLUE_EX}files defined in the system ")

    tnmd = 0
    i = 0
    while len(database.split()) > i:
        if os.path.exists(database.split()[i]):
            tnmd = tnmd + 1
            # burada dosyaları kopyala
        i = i + 1
    print(f"{Fore.GREEN}{tnmd} {Fore.LIGHTBLUE_EX}identified files/folders were detected and backed up")
    
    time.sleep(3)
    
mainProcess = threading.Thread(target=main)
mainProcess.start()
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
██▓▓░░░░░░░░░░░░░░░░░░░░░░░░██  
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

mainProcess.join()
os.system(cleaner)

print(f'{Fore.CYAN}The backup is complete! What would you like to do now?')
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
ARES ARES      {Fore.CYAN}{version}{Fore.LIGHTGREEN_EX}  
ARES  ARES     {Fore.CYAN}{Os}{Fore.LIGHTGREEN_EX}
ARES   ARES    {Fore.CYAN}{loader}{Fore.LIGHTGREEN_EX}
ARES    ARES   {Fore.CYAN}GNU{Fore.LIGHTGREEN_EX}
ARES     ARES     
ARES      ARES    
''')
    time.sleep(2)
    exit()