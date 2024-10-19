#include <iostream>
#include <windows.h>
#include <lmcons.h>
#include <tchar.h>
#include <sys/stat.h>
#include <ctime>  // <ctime> kütüphanesini ekleyelim

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

int main() {
    const char* file_path = "example.txt";  // Kontrol edilecek dosya

    // 1. Dosyanýn tam yolu
    char full_path[MAX_PATH];
    if (GetFullPathName(file_path, MAX_PATH, full_path, NULL)) {
        std::cout << "Full Path: " << full_path << "\n";
    }
    else {
        std::cerr << "Error getting full path.\n";
    }

    // 2. Dosya özniteliklerini al
    DWORD attributes = GetFileAttributes(file_path);
    if (attributes == INVALID_FILE_ATTRIBUTES) {
        std::cerr << "Error: Could not get file attributes.\n";
    }
    else {
        std::cout << "Attributes: ";
        print_file_attributes(attributes);
    }

    // 3. Dosya sahibi
    TCHAR username[UNLEN + 1];
    DWORD username_len = UNLEN + 1;
    if (GetUserName(username, &username_len)) {
        std::cout << "Owner: " << username << "\n";
    }
    else {
        std::cerr << "Error getting file owner.\n";
    }

    // 4. Dosyanýn boyutu ve son deðiþtirilme tarihi için POSIX `stat` kullanýmý
    struct stat file_info;
    if (stat(file_path, &file_info) == 0) {
        std::cout << "Size: " << file_info.st_size << " bytes\n";
        std::cout << "Last Modified: " << ctime(&file_info.st_mtime);  // std::ctime olmadan
    }
    else {
        std::cerr << "Error: Could not access file.\n";
    }

    bool loop = true;
    cin >> loop;

    return 0;
}
