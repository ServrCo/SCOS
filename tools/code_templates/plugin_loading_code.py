# place this code in the correct places in your SCOS component to add plugin compatibility.

# HEADERS
import importlib.util
SCOS_root = "/SCOS/"
pluginsConfigFolderName = "sysConfig/pluginLists/"
allPluginObjs = []

pluginListFile = open(SCOS_root + pluginsConfigFolderName + "userland.pluginList") # replace this filename with correct plugin list name 
pluginList = pluginListFile.read().split("\n")

for pluginPath in pluginList:
    if pluginPath != "":
        spec = importlib.util.spec_from_file_location("*", pluginPath)
        instance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(instance)
        allPluginObjs.append(instance)

def event_to_plugins(eventString):
    for instance in allPluginObjs:
        instance.event(eventString)

# before Tkinter mainloop
for instance in allPluginObjs:
    instance.uiObject(your_tkinter_main_object_here) 

event_to_plugins("ready")
