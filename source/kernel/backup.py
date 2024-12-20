import os
import shutil
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def backup_files():
    try:
        with open('source/kernel/database', 'r') as file:
            directories = file.read().strip().split('\n')

        backup_dir = os.path.join(os.getcwd(), 'backup')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        for directory in directories:
            if os.path.exists(directory):
                destination_dir = os.path.join(backup_dir, os.path.basename(directory))
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                for root, dirs, files in os.walk(directory):
                    for file in files:
                        src_file = os.path.join(root, file)
                        relative_path = os.path.relpath(root, directory)
                        dest_path = os.path.join(destination_dir, relative_path)

                        if not os.path.exists(dest_path):
                            os.makedirs(dest_path)

                        shutil.copy2(src_file, dest_path)

                print(Fore.GREEN + f"Dizin başarıyla yedeklendi: {directory}")
            else:
                print(Fore.RED + f"Dizin bulunamadı: {directory}")
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")


if __name__ == "__main__":
    backup_files()
