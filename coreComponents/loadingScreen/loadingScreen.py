import os, sys
from tkinter import *
from time import sleep

loadingScreen = Tk()
loadingScreen.title("SCOS Loading Screen")

w, h = loadingScreen.winfo_screenwidth(), loadingScreen.winfo_screenheight()

Canvas(loadingScreen, bg="#000000", width=w, height=h).place(relx=0.5, rely=0.5, anchor="c")
Label(loadingScreen, text="Servr Co OS", bg="#000000", fg="#ffffff", font=("Ubuntu", 40)).place(relx=0.5, rely=0.5, anchor="c")
# Let's set this to full screen, as we well should.
loadingScreen.attributes("-fullscreen", True)
loadingScreen.attributes("-zoomed", True)

loadingScreen.mainloop()
