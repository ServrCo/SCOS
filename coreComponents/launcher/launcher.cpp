/* 
// launcher.cpp - all startup functions are handled here.
// This code launches the login screen, and waits for it to terminate.
// If the login screen terminates with a non-zero exit code, it launches the crash screen
// (this helps mitigate a security hole which allowed bypassing of the login screen.)
// If the login screen terminates with an exit code of zero, it is safe to continue on and launch userland-ui, the SCOS desktop environment.
*/
#include <iostream>
#include <fstream>
#include <string>
#include <thread>
std::string buildNum = "0.1";

using namespace std;

void showLoadingScreen() {
    system("cd core;python3 loadingScreen.py");
}

void showCrashScreen() {
    int crashScreenExitCode = system("cd core;python3 crashScreen.py");
}

int main() {
    while (true) {
        cout << "Launching Servr Co OS.\nBUILD: " + buildNum + "\n";

        if (system("cd core; python3 startupRoutine.py") != 0){
            showCrashScreen();
            continue;
        }

        system("cd core;python3 pluginInitializer.py");

        int loginScreen = system("cd desktopEnv/LogonUI/;python3 LogonUI.py");
        if (loginScreen != 0) {
            showCrashScreen();
            continue;
        }
        else {
            int userland = system("cd desktopEnv;python3 userland-ui.py");
            if (userland != 0) {
                showCrashScreen();
            }
        }
    }
}
