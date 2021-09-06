uiWindow = []
from tkinter import *
import os

def crash(event):
	sys.exit(2)

def event(eventString):
	if eventString == "ready":
		uiWindow.bind_all("<F12>", func=crash)

def uiObject(obj):
	global uiWindow
	uiWindow = obj
