# pluginInitializer.py
# discovers Servr Co OS plugins, their file paths, and where to load them.
# upon discovery of plugins, it puts their paths in several text files that tell the system to load them.

import os, sys, json
from configparser import ConfigParser
config = ConfigParser()
SCOS_root = "/SCOS/"
SCOS_configs_root = "/SCOS/sysConfig/"
pluginsFolderName = "plugins/"
# logFile = open(SCOS_root + "logs/pluginInitializer.log", "a")

# create all files that need to be created
for filename in ["userland.pluginList", "loginScreen.pluginList", "crashScreen.pluginList"]:
    cur_file = open(SCOS_configs_root + "pluginLists/" + filename, "w+")
    cur_file.write("")
    cur_file.close()

def report_error(error_type, shouldLog, message):
    errorString = error_type + " " + "PLUGIN ERROR: " + message
    print(errorString)
    # if shouldLog:
    #     logFile.write(errorString + "\n")
        
    #TODO: implement error screen triggering

for folder in os.listdir(SCOS_root + pluginsFolderName + "."):
    if os.path.isdir(SCOS_root + pluginsFolderName + folder):
        pluginToInspect = SCOS_root + pluginsFolderName + folder + "/"
        print("INSPECTING PLUGIN: " + pluginToInspect)

        config.read(pluginToInspect + "plugin.config")

        cur_list_file = open(SCOS_configs_root + "pluginLists/" + config.get("plugin", "load_at") + ".pluginList", "a")
        cur_list_file.write(pluginToInspect + config.get("plugin", "main_file") + "\n")
        
        try:
            # open the correct plugin list file and write the plugin path
            pass
        
        except:
            report_error("NON-FATAL", True, "Failed to initialize plugin at " + pluginToInspect + ": don't know where to load plugin!")
            continue
        #TODO: implement plugin loading into code




# from configparser import ConfigParser
# config = ConfigParser()

# config.read('config.ini')
# config.add_section('main')
# config.set('main', 'key1', 'value1')
# config.set('main', 'key2', 'value2')
# config.set('main', 'key3', 'value3')

# with open('config.ini', 'w') as f:
#     config.write(f)