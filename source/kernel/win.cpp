#include <iostream>
#include <fstream>
#include <string>
#include <thread>
#include <chrono>
#include <filesystem>

using namespace std;

bool fileExists(const string& filename) {
    return filesystem::exists(filename); 
}

void copyDirectory(const filesystem::path& source, const filesystem::path& target) {
    for (const auto& entry : filesystem::directory_iterator(source)) {
        const auto& path = entry.path();
        filesystem::copy(path, target / path.filename(), filesystem::copy_options::overwrite_existing | filesystem::copy_options::recursive);
    }
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();

    filesystem::path timeFile = "kernel/time";
    ofstream file(timeFile);
    if (!file) {
        cerr << "err 007" << endl;
        return 1;
    }

    filesystem::path filename = "kernel/database";

    if (!fileExists(filename.string())) {
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
        n++;
        cout << "line" << n << " " << line << endl;

        filesystem::path sourceDir = line;
        filesystem::path targetDir = "backup/";

        try {
            copyDirectory(sourceDir, targetDir);
            cout << "DONE!" << endl;
        } catch (const filesystem::filesystem_error& e) {
            cerr << "err 005" << endl;
            return 1;
        } catch (const exception& e) {
            cerr << "err 004" << endl;
            return 1;
        }
    }

    inputFile.close();

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
    file << duration.count() << endl;
    file.close();

    return 0;
}
