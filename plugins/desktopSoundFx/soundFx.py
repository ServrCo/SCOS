uiWindow = []
from tkinter import *
import os
try:
	import pygame
except:
	os.system("pip install pygame")
	import pygame

pygame.mixer.init(44100, -16, 2, 64)

startupSound = pygame.mixer.Sound(os.path.split(__file__)[0] + "/startup.wav")
clickSound = pygame.mixer.Sound(os.path.split(__file__)[0] + "/mouseclick.wav")

def event(eventString):
	if eventString == "ready":
		startupSound.play()
	if eventString == "actionmenu-create":
		clickSound.play()

def uiObject(obj):
	global uiWindow
	uiWindow = obj

print(os.path.split(__file__)[0])
