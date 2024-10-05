#include <iostream>
#include <string>
#include <windows.h>

bool virusTotal = false;

using namespace std;

void databaseScanner() {
    // Veri Tabanındaki tehditlerle uyumu kontrol edecektir
}


void setConsoleColor(int textColor, int bgColor) {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, textColor | (bgColor << 4));
}

bool hasVirusSignature(const std::string& fileName) {
    return fileName.find("virus") != std::string::npos || fileName.find("malware") != std::string::npos;
}

bool isSystemFile(const std::string& fileName) {
    return fileName == "System Volume Information" ||
        fileName == "pagefile.sys" ||
        fileName == "hiberfil.sys" ||
        fileName == "swapfile.sys" ||
        fileName == "ProgramData";
}

bool isUserCreatedFile(const std::string& fileName) {
    return fileName == "virus.txt";
}

void scanDirectory(const std::string& directory) {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile((directory + "\\*").c_str(), &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        setConsoleColor(14, 0);
        std::cerr << "Blocked: " << directory << std::endl;
        return;
    }

    do {
        const std::string fileName = findFileData.cFileName;

        if (fileName != "." && fileName != "..") {
            if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
                scanDirectory(directory + "\\" + fileName);
            }
            else {
                if (hasVirusSignature(fileName)) {
                    if (!isSystemFile(fileName) && !isUserCreatedFile(fileName)) {
                        setConsoleColor(12, 0);
                        std::cout << "Found potential file: " << directory + "\\" + fileName << std::endl;
                        setConsoleColor(7, 0);
                    }
                }
            }
        }
    } while (FindNextFile(hFind, &findFileData) != 0);

    FindClose(hFind);
}

int main() {
    std::string startPath = "D:\\"; 
    scanDirectory(startPath);

    cout << endl;
    cout << "first scan is complete!" << endl;
    cout << ""
    int loop;
    cin >> loop;
    return 0;
}
