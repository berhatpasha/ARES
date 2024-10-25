#include <iostream>
#include <fstream>
#include <string>
#include <sys/stat.h>
#include <thread>
#include <chrono>
#include <filesystem>

using namespace std;

bool fileExists(const string &filename) {
    struct stat buffer;   
    return (stat(filename.c_str(), &buffer) == 0); 
}

void copyDirectory(const filesystem::path& source, const filesystem::path& target) {

    for (const auto& entry : filesystem::directory_iterator(source)) {
        const auto& path = entry.path();
        filesystem::copy(path, target / path.filename(), filesystem::copy_options::overwrite_existing | filesystem::copy_options::recursive);
    }
}

int main() {
    string filename = "database";

    if (!fileExists(filename)) {
        cerr << "err" << endl;
        return 1;
    }

    ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        cerr << "err" << endl;
        return 1;
    }

    int n = 0;

    string line;
    while (getline(inputFile, line)) {
        n ++;
        cout << "satır" << n << " " << line << endl;
        string sourceDir = line;
        string targetDir = "../backup/";


        try {
            copyDirectory(sourceDir, targetDir);
            std::cout << "DONE!" << std::endl;
        } catch (const filesystem::filesystem_error& e) {
            std::cerr << "ERR" << std::endl;
            return 1;
        } catch (const std::exception& e) {
            std::cerr << "ERR" << std::endl;
            return 1;
        }
    }

    inputFile.close();
    return 0;
}
