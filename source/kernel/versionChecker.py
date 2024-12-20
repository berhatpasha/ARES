import requests
import time

thisVersion = "ALPHA 1.0.0"
FILE_URL = "https://raw.githubusercontent.com/berhatpasha/ARES/refs/heads/main/source/kernel/version"
CHECK_INTERVAL = 5

def fetch_file_content():
    try:
        response = requests.get(FILE_URL)
        if response.status_code == 200:
            return response.text.strip() 
        else:
            print(f"Hata: {response.status_code} - {response.reason}")
            return None
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return None

def monitor_file():
    last_content = None
    while True:
        print("Checking..")
        content = fetch_file_content()
        if content is not None:
            if str(content) != str(thisVersion):
                print(f"NEW UPTADE:\n{content} your:{thisVersion}")
                last_content = content
            else:
                print(f"current ++ last:{last_content} your:{thisVersion}")
        else:
            print("err")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_file()
