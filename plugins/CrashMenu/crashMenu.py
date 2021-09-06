uiWindow = []
from tkinter import *
import os, sys

def showDangerousOptions():
	dangerousOptions = Tk()
	dangerousOptions.title("SCOS Crash Menu- dangerous options")
	dangerousOptions.attributes("-zoomed", 1)
	dangerousOptions.attributes("-fullscreen", 1)
	w,h = dangerousOptions.winfo_screenwidth(), dangerousOptions.winfo_screenheight()
	Canvas(dangerousOptions, bg="#0000ff", width=w, height=h).place(relx=0.5, rely=0.5, anchor="c")
	def closeDangerousFunctions():
		dangerousOptions.destroy()
	Button(dangerousOptions, text="x", command=closeDangerousFunctions).place(relx=0.99, rely=0.01, anchor="n")
	Label(dangerousOptions, text="DANGEROUS OPTIONS", font=("Ubuntu", 15)).place(relx=0.5, rely=0.05, anchor="n")
	Label(dangerousOptions, text="THESE COULD DAMAGE YOUR COPY OF SERVR CO OS.\nONLY USE IF YOU KNOW WHAT YOU'RE DOING.", font=("Ubuntu", 10)).place(relx=0.5, rely=0.1, anchor="n")


def openCrashMenu():
	menuWindow = Tk()
	menuWindow.title("SCOS Crash Menu")
	menuWindow.attributes("-zoomed", 1)
	menuWindow.attributes("-fullscreen", 1)

	
	def closeCrashMenu():
		menuWindow.destroy()

	def restartSCOS():
		sys.exit(0)

	def exitSCOS():
		os.system("pkill launcher")
		sys.exit()

	Label(menuWindow, text="SCOS Crash Menu").place(relx=0.5, rely=0.05, anchor="n")
	Button(menuWindow, text="x", command=closeCrashMenu).place(relx=0.99, rely=0.01, anchor="n")

	Label(menuWindow, text="BASIC FUNCTIONS").place(relx=0.1, rely=0.1, anchor="n")
	Button(menuWindow, text="restart SCOS", command=restartSCOS).place(relx=0.1, rely=0.15, anchor="n")
	Button(menuWindow, text="exit to core desktop", command=exitSCOS).place(relx=0.1, rely=0.2, anchor="n") #TODO: implement
	Button(menuWindow, text="display dangerous functions", command=showDangerousOptions).place(relx=0.1, rely=0.25, anchor="n")

def event(eventString):
	print("Caught an event: " + eventString)
	if eventString == "ready":
		Button(uiWindow, text="Open Crash Menu", command=openCrashMenu).place(relx=0.5, rely=0.65, anchor="n")

def uiObject(obj):
	global uiWindow
	uiWindow = obj

class crashMenuButtons:
	def closeMenu(self, menuWindow):
		menuWindow.destroy()
