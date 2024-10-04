#include <windows.h>
#include <wincrypt.h>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>

const std::vector<std::string> keywords = {
    "memz", "virus", "viruses", "trojan", "worm", "malware", "ransomware", "spyware", 
    "adware", "keylogger", "botnet", "phishing", "rootkit", "backdoor", "exploit",
    "payload", "infector", "zbot", "agent", "payloads", "vundo", "conficker",
    "crypto", "badrabbit", "locky", "wannacry", "cryptolocker", "zeus", 
    "nimda", "mydoom", "sasser", "stuxnet", "blaster", "iloveyou", "petya",
    "darkhotel", "emotet", "dridex", "trickbot", "mercury", "nephalem",
    "cerber", "phorpiex", "qbot", "kraken", "darkside", "blackmatter",
    "gamarue", "sality", "bagle", "gafgyt", "safebrowsing", "hummingbad",
    "kryptik", "sydra", "moskito", "skynet", "redline", "infostealer",
    "rbot", "spy", "darktrace", "sneaky", "scrypt", "nuke", "bot",
    "dork", "stealer", "pupy", "cabal", "sentry", "smokeloader"
};

bool IsFileSigned(const std::string& filePath) {
    HANDLE hFile = CreateFile(filePath.c_str(), GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
        return false;
    }

    DWORD dwFileSize = GetFileSize(hFile, NULL);
    if (dwFileSize == INVALID_FILE_SIZE) {
        CloseHandle(hFile);
        return false;
    }

    WINTRUST_FILE_INFO fileInfo = {};
    fileInfo.cbStruct = sizeof(fileInfo);
    fileInfo.pcwszFilePath = std::wstring(filePath.begin(), filePath.end()).c_str();
    fileInfo.hFile = NULL;

    GUID guidAction = WINTRUST_ACTION_GENERIC_VERIFY_V2;
    WINTRUST_DATA winTrustData = {};
    winTrustData.cbStruct = sizeof(winTrustData);
    winTrustData.dwUIChoice = WTD_UI_NONE;
    winTrustData.fdwRevocationChecks = WTD_REVOKE_NONE;
    winTrustData.dwUnionChoice = WTD_CHOICE_FILE;
    winTrustData.pFile = &fileInfo;

    LONG lStatus = WinVerifyTrust(NULL, &guidAction, &winTrustData);
    CloseHandle(hFile);

    return (lStatus == ERROR_SUCCESS); 
}

// Anahtar kelime kontrol fonksiyonu
bool ContainsKeyword(const std::string& filePath) {
    std::ifstream file(filePath);
    std::string line;

    while (std::getline(file, line)) {
        for (const auto& keyword : keywords) {
            if (line.find(keyword) != std::string::npos) {
                return true; 
            }
        }
    }
    return false;
}

void GetFilesInDirectory(const std::string& directory, std::vector<std::string>& files) {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile((directory + "\\*").c_str(), &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        std::cerr << "passed" << std::endl;
        return;
    }

    do {
        const std::string fileName = findFileData.cFileName;
        if (fileName != "." && fileName != "..") {
            std::string fullPath = directory + "\\" + fileName;
            if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
                GetFilesInDirectory(fullPath, files);
            } else {
                files.push_back(fullPath);
            }
        }
    } while (FindNextFile(hFind, &findFileData) != 0);

    FindClose(hFind);
}

int main() {
    cout << endl;
    cout << "Scanning service launched" << endl;

    std::vector<std::string> filesToScan;
    GetFilesInDirectory("C:\\Path\\to\\directory", filesToScan);

    for (const auto& file : filesToScan) {
        if (!IsFileSigned(file) && ContainsKeyword(file)) {
            std::cout << "Threatening file: " << file << std::endl;
        }
    }

    return 0;
}
