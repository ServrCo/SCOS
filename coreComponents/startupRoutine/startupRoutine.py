# startupRoutine.py
# ran before pluginInitializer on every system startup.

import os, sys

SCOS_root = os.path.abspath("../")
SCOS_plugin_root = os.path.abspath("../plugins")
SCOS_configs_root = os.path.abspath("../sysConfig")
directories_to_make = ["../sysConfig/pluginLists", "../sysconfig/apps"]
# Initialize our environment variables (issue: doesn't apply to other code, is semi-useless outside of this file)
os.environ["SCOS_root"] = SCOS_root
os.environ["SCOS_plugin_root"] = SCOS_plugin_root
os.environ["SCOS_configs_root"] = SCOS_configs_root

# make sure these directories exist
for directory in directories_to_make:
    try:
        os.mkdir(directory)
    except:
        pass

if os.system("cd $SCOS_configs_root") != 0: # If config files don't exist, things will go wrong. Display crash screen.
    errorfile = open(SCOS_root + "/errorfile", "w+")
    errorfile.write("SCOS.NoConfigDirectory")
    errorfile.close()
    sys.exit(1)
