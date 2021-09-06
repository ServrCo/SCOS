# SCOS binGen
# handles and generates build images

import os, sys, shutil, random
from configparser import ConfigParser
config = ConfigParser()
config.read("config/binGen.config")

binsPath = os.path.abspath("../bins")
workingDir = config.get("initialize", "workdir")
try:
    shutil.rmtree(workingDir)
except:
    pass

os.mkdir(workingDir)

dirs_to_copy = [
[binsPath + "/launcher/.", workingDir + "/"],
[binsPath + "/core/.", workingDir + "/core/"],
[binsPath + "/desktopEnv/.", workingDir + "/desktopEnv/"],
[binsPath + "/plugins/.", workingDir + "/plugins/"],
[binsPath + "/../config/defaults/.", workingDir + "/sysConfig/"],
# [binsPath + "/../vinyl/desktopEnv/.", workingDir + "/desktopEnv/"], # remove for non-vinyl releases
]

for currentDir in dirs_to_copy:
    os.system("mkdir -p " + currentDir[1])
    os.system("cp -r " + currentDir[0] + " " + currentDir[1])

if "install-only" in sys.argv:
    os.system("sudo cp -R %s/. /SCOS;sudo chown -R $USER /SCOS" % (workingDir))
    print("Installed!")

if "make-image" in sys.argv:
    imageType = config.get("image", "imageTarget")
    print("Generating image of type: " + imageType)

    imageFilename = "SCOS-" + imageType + "-" + config.get("image", "imageVersion") + "-" + str(random.randint(1111, 9999)) + ".7z"
    print("Output filename: " + imageFilename)

    print("Making 7z image of OS")
    os.system("7z a installerWorkDir/SCOS.7z workdir/.")

    print("Making command line installer image")
    os.system("cp ./install installerWorkDir/.")
    os.system("7z a %s installerWorkDir/." % (config.get("initialize", "outputdir") + "/" + imageFilename))

if "cleanup" in sys.argv:
    try:
        shutil.rmtree("workdir")
        shutil.rmtree("installerWorkDir")
        print("cleanup succeeded")

    except:
        print("cleanup failed")