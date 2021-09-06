import os
import time
import shutil
ignoreFolders = ["bins", "tools", "old", "config", "binGen", "api", "vinyl"]
binPath = "bins"

def time_elapsed():
    print("TIME ELAPSED: " + str(time.process_time()))

print("Preparing for build.")
os.environ["SCOSBuildPath"] = os.path.abspath(binPath)

try:
    shutil.rmtree(binPath)
except:
    print("This must be your first build. Welcome aboard!")

try:
    os.mkdir(binPath)
except:
    print("Error when creating bins folder.")

dirs = [name for name in os.listdir(".") if os.path.isdir(name) and name not in ignoreFolders]

for folder in dirs:
    print("BUILDING: "+folder)
    os.system("cd "+ folder + ";make")

time_elapsed()
