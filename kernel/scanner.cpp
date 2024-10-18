#include <iostream>
#include <string>
#include <windows.h>

bool virusTotal = false;

using namespace std;

void print_file_attributes(DWORD file_attributes) {
    if (file_attributes & FILE_ATTRIBUTE_ARCHIVE)
        std::cout << "Archive ";
    if (file_attributes & FILE_ATTRIBUTE_HIDDEN)
        std::cout << "Hidden ";
    if (file_attributes & FILE_ATTRIBUTE_READONLY)
        std::cout << "Read-only ";
    if (file_attributes & FILE_ATTRIBUTE_SYSTEM)
        std::cout << "System ";
    std::cout << "\n";
}
/*
bool databaseScanner(file_path) {
    // Veri tabanını çek ve veri tabanı ile karşılaştırma yap :

    char full_path[MAX_PATH];
    if (GetFullPathName(file_path, MAX_PATH, full_path, NULL)) {
        std::cout << "Full Path: " << full_path << "\n";
    }
    else {
        std::cerr << "Error getting full path.\n";
    }

    DWORD attributes = GetFileAttributes(file_path);
    if (attributes == INVALID_FILE_ATTRIBUTES) {
        std::cerr << "Error: Could not get file attributes.\n";
    }
    else {
        std::cout << "Attributes: ";
        print_file_attributes(attributes);
    }

    TCHAR username[UNLEN + 1];
    DWORD username_len = UNLEN + 1;
    if (GetUserName(username, &username_len)) {
        std::cout << "Owner: " << username << "\n";
    }
    else {
        std::cerr << "Error getting file owner.\n";
    }

    struct stat file_info;
    if (stat(file_path, &file_info) == 0) {
        std::cout << "Size: " << file_info.st_size << " bytes\n";
        std::cout << "Last Modified: " << ctime(&file_info.st_mtime);  // std::ctime olmadan
    }
    else {
        std::cerr << "Error: Could not access file.\n";
    }

    return 0;
}
*/

void setConsoleColor(int textColor, int bgColor) {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, textColor | (bgColor << 4));
}

bool hasVirusSignature(const std::string& fileName) {
    return fileName.find("virus") != std::string::npos || fileName.find("malware") != std::string::npos;
}

bool isSystemFile(const std::string& fileName) {
    return fileName == "System Volume Information" || fileName == "pagefile.sys" || fileName == "hiberfil.sys" || fileName == "swapfile.sys" || fileName == "ProgramData";
}

bool isUserCreatedFile(const std::string& fileName) {
    return fileName == "virus.txt";
}

void scanDirectory(const std::string& directory) {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile((directory + "\\*").c_str(), &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        setConsoleColor(8, 0);
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
                        setConsoleColor(6, 0);
                    }
                }
            }
        }
    } while (FindNextFile(hFind, &findFileData) != 0);

    FindClose(hFind);
}

int main() {
    std::string startPath = "C:\\Windows\\"; 
    scanDirectory(startPath);

    cout << endl;
    cout << "scan is complete!" << endl;
    cout << "";
    int loop;
    cin >> loop;
    return 0;
}
