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
    auto start = std::chrono::high_resolution_clock::now();

    ofstream file("kernel/time");
    if (!file) {
        std::cerr << "err 007" << std::endl;
        return 1;
    }

    string filename = "kernel/database";

    if (!fileExists(filename)) {
        cerr << "err 002" << endl;
        return 1;
    }

    ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        cerr << "err 003" << endl;
        return 1;
    }

    int n = 0;

    string line;
    while (getline(inputFile, line)) {
        n ++;
        cout << "line" << n << " " << line << endl;
        string sourceDir = line;
        string targetDir = "backup/";


        try {
            copyDirectory(sourceDir, targetDir);
            std::cout << "DONE!" << std::endl;
        } catch (const filesystem::filesystem_error& e) {
            std::cerr << "err 005" << std::endl;
            return 1;
        } catch (const std::exception& e) {
            std::cerr << "err 004" << std::endl;
            return 1;
        }
    }

    inputFile.close();

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    file << duration.count() << std::endl;
    file.close();

    return 0;
}

