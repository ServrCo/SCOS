#include <iostream>
#include <thread>
#include <string>

using namespace std;
int main() {
    int shouldContinue = 1;
    cout << "Launching installer.\n";
    
    if (shouldContinue == 1) {
        cout << "Extracting sources...\n";
        system("mkdir -p extracted;cd extracted;7z x ../SCOS.7z");
        cout << "Sources extracted. Moving to installation directory.\n";
        system("sudo cp -R extracted/. /SCOS;sudo chown -R $USER /SCOS");
        cout << "Installing dependencies...\n";
        system("sudo apt install python3-tk python3-pil.imagetk python-dotenv");
        cout << "Done installing!\n";
    }
}
