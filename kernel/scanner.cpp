// imzasız olan dosyalar için tarama yapmalı


#include <iostream>
#include <thread>
#include <chrono>
#include <string>
#include <filesystem>
#include <fstream>
#include <vector>

using namespace std;
namespace fs = std::filesystem;

bool searchInFile(const fs::path& filePath, const std::vector<std::string>& keywords) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Cannot open file: " << filePath << std::endl;
        return false;
    }

    std::string line;
    while (std::getline(file, line)) {
        for (const auto& keyword : keywords) {
            if (line.find(keyword) != std::string::npos) {
                std::cout << "Keyword \"" << keyword << "\" found in file: " << filePath << std::endl;
                return true;
            }
        }
    }
    return false;
}


void scanSystem(const std::vector<std::string>& keywords) {
    for (const auto& entry : fs::recursive_directory_iterator("/")) {
        if (fs::is_regular_file(entry)) {
            searchInFile(entry.path(), keywords);
        }
    }
}

int main(){
    cout << endl;
    cout << "Scanning process initiated" << endl;

std::vector<std::string> keywords = {
    "Memz",              
    "ILOVEYOU",         
    "MyDoom",          
    "Sasser",           
    "Conficker",        
    "Nimda",             
    "Stuxnet",          
    "Cryptolocker",    
    "WannaCry",        
    "Ransomware",       
    "Zeus",             
    "Trojan",           
    "Spyware",         
    "Adware",           
    "Backdoor",       
    "Keylogger",         
    "Virus",            
    "Phishing",          
    "Rootkit",           
    "Botnet",           
    "Fidye",            
    "Bagle",            
    "Blaster",          
    "Klez",              
    "Slammer",          
    "Rbot",              
    "Spybot",          
    "DarkComet",        
    "Havex",            
    "Sality",           
    "Sality",          
    "Dridex",           
    "Dorkbot",          
    "Ransom",            
    "Simda",             
    "Tinba",            
    "Gamarue",        
    "Kovter",          
    "Kryptik",          
    "PushNotification",  
    "W32/Conficker",    
    "Trojans",          
    "Bait and Switch",  
    "DDoS",             
    "Kryptik",          
    "Locky",            
    "Ransomware",        
    "Mirai",            
    "Bluesnarfing",      
    "Phish",           
    "AdClick",          
    "Formjacking",      
    "HTML/Phishing",    
    "Eko",             
    "Mimic",           
    "Mamba",             
    "Ramnit",          
    "Shylock",         
    "Sasser",            
    "Gamarue",          
    "Locky",            
    "Kovter",            
    "Andromeda",        
    "Bait and Switch",   
    "CryptXXX",         
    "Scrypt",          
    "Buhtrap",          
    "Syndicate",        
    "Bifrose",          
    "Rafale",           
    "Unreal",           
    "Kryptik",          
    "FBI Ransom",       
    "Scareware",        
    "Faker",            
    "Netsky",           
    "Funner",            
    "ZeuS",              
    "Simda",             
    "Hesperbot",       
    "Fakem",             
    "Nuke",             
    "Downadup",          
    "Kak",               
    "Fennel",            
    "Ngrbot",            
    "Genie",            
    "DarkComet",       
    "Crypt",            
    "W32/Blaster",      
    "Koobface",         
    "DDoS",             
    "FakeAV",          
    "Fugue",         
    "Zero-Day",         
    "Trojan.Win32",     
    "Malicious",      
    "W32/Sasser",       
};


    scanSystem(keywords);

    return 0;

}