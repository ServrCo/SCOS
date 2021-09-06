# This is the main Python file for the SCOS-Userland section of the OS.

from tkinter import *
from runpy import run_path
import sys, importlib.util

uiWindow = Tk()
uiWindow.title("Servr Co OS Userland")

SCOS_root = "/SCOS/"
pluginsFolderName = "plugins/"
allPluginObjs = []
uiWindow.attributes("-fullscreen", True)
uiWindow.attributes("-zoomed", True)

# PLUGINS
# Servr Co OS plugins are a simplistic mess. Just remember that before scrolling through this code.
pluginListFile = open(SCOS_root + pluginsFolderName + "userland.pluginList")
pluginList = pluginListFile.read().split("\n")

# load and initialize plugin
for pluginPath in pluginList:
    if pluginPath != "":
        # pluginInstance = run_path(plugin)
        # print(pluginInstance)

        spec = importlib.util.spec_from_file_location("*", pluginPath)
        instance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(instance)
        allPluginObjs.append(instance)
        # instance.send_ui_object(uiWindow)



def event_to_plugins(eventString):
    for instance in allPluginObjs:
        instance.event(eventString)

# DESKTOP BACKGROUND
background_image = PhotoImage(file="./rsrc/img/bgs/vinyl.png")
background_image_container = Label(uiWindow, image=background_image)
background_image_container.place(relx=0.5, rely=0.5, anchor="c")
background_image_container.image = background_image

# TOOLBAR
def actionButtonCallback():
    drawMenu()

Canvas(uiWindow, width=uiWindow.winfo_screenwidth(), height=int(uiWindow.winfo_screenheight()) - uiWindow.winfo_screenheight()/1.04).place(anchor="nw") # Make and load a white rectangle at the top of the window for the toolbar.
#TODO: Add the ability to enable Dark Theme, which makes the bar black when active. This could be a simple setting once the Settings app is made.

actionButton = Button(uiWindow, text="Action Button", command=actionButtonCallback)
timeClockLabel = Label(uiWindow, text="Cl:oc:k.")

timeClockLabel.place(relx=1, rely=0.01, anchor="ne")
actionButton.grid(row=0, column=0)

# ACTION MENU
#TODO: only allow menu to be drawn once
def drawMenu():
    event_to_plugins("actionmenu-create")
    def endSessionCallback():
        uiWindow.destroy()

    def aboutAppCallback(uiWindow):
        uiWindow.attributes("-fullscreen", True)
        uiWindow.attributes("-zoomed", True)
    
    menuBackground = Canvas(uiWindow, width=uiWindow.winfo_screenwidth()/3, height=uiWindow.winfo_screenheight()/2)
    menuBackground.place(rely=0.04)

    endSessionButton = Button(uiWindow, text="Log Out", command=endSessionCallback)
    endSessionButton.place(relx=0.1,rely=0.5)

    def destroyMenu():
        event_to_plugins("actionmenu-destroy")
        menuBackground.destroy()
        endSessionButton.destroy()
        destroyExitButton()

    exitMenuButton = Button(uiWindow, text="Exit Menu", command=destroyMenu)
    exitMenuButton.place(rely=0.5)

    def destroyExitButton():
        exitMenuButton.destroy()

# uiWindow object to plugins
for instance in allPluginObjs:
    instance.uiObject(uiWindow)

event_to_plugins("ready")

uiWindow.mainloop()
event_to_plugins("userland-terminate")
