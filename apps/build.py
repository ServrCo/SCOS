import os

try:
    os.mkdir("bins")
except:
    pass

os.envrion["appsBuildDir"] = os.path.abspath("bins")

dirs = [name for name in os.listdir(".") if os.path.isdir(name)]

for folder in dirs:
    print("BUILDING: "+folder)
    os.system("cd "+ folder + ";make")
