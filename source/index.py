import subprocess
import threading
import os 
import time
import colorama
import shutil
from colorama import Fore
colorama.init(autoreset=True)

disk = os.getcwd()[0]

if disk == "/" or disk == "C:":
    print(f"{Fore.RED} incorrect installation or false start err : 001")
    time.sleep(3)
    exit()

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
    

def ejectDisk_Windows(disk_letter):
    command = f"powershell -Command \"(New-Object -COMObject Shell.Application).Namespace('{disk_letter}').Self.InvokeVerb('Eject')\""
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{disk_letter} diski çıkartıldı.")
    except subprocess.CalledProcessError as e:
        print(f"err: {e}")

    
backup_path = os.path.join(os.getcwd(), 'backup')
def main():
    time.sleep(2.5)
    print(f"{Fore.CYAN}recovery in progress: ")
    print(f"{Fore.GREEN}{len(database.split())} {Fore.LIGHTBLUE_EX}files defined in the system ")


    tnmd = 0
    for path in database.split():
        if not os.path.exists(path):
            print(f"{path} NOT FOUND (passed)")
            continue 
        for root, dirs, files in os.walk(path):
            for file in files:
                srcFile = os.path.join(root,file)
                destFile = os.path.join(backup_path, os.path.relpath(srcFile, path))
                
                try:
                    os.makedirs(os.path.dirname(destFile), exist_ok=True)
                    shutil.copy2(srcFile, destFile)
                    tnmd += 1
                except:
                    print(f"err passed")
                    time.sleep(3)    
            for dir in dirs:
                src_dir = os.path.join(root,dir)
                dest_dir = os.path.join(backup_path, os.path.relpath(src_dir,path))
                try:
                    os.makedirs(dest_dir, exist_ok=True)
                except:
                    print(f"err passed")
    
    print(f"{Fore.GREEN}{tnmd} {Fore.LIGHTBLUE_EX}identified files/folders were detected and backed up")
    time.sleep(4)

    
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
    if os=="windows":
        pass
        ejectDisk_Windows(f"{os.getcwd()[0]}")
    else:
        pass
        subprocess.run('umount', f"/media/{username}/E", check=True)
    exit()
    