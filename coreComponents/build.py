import os

dirs = [name for name in os.listdir(".") if os.path.isdir(name)]

for folder in dirs:
    print("BUILDING: "+folder)
    os.system("cd "+ folder + ";make")
