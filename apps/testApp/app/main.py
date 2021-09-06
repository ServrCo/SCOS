from tkinter import *
import SCOS.UI
import os

main = SCOS.UI.SCOSApp(title="test - Servr Co OS", width=300, height=400)
main.mainloop()

def callback(event):
	print(event)
