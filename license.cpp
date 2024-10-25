#include <iostream>
#include <fstream>  

int main() {
    std::ifstream inputFile("license"); 


    if (!inputFile.is_open()) {
        std::cerr << "err" << std::endl;
        return 1;
    }

    std::string line;

    while (std::getline(inputFile, line)) {
        std::cout << line << std::endl;
    }

    inputFile.close();  
    return 0;
}
