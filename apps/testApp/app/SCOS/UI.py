from tkinter import *
appObj = []
toolbarBgObj = []
titleLabelObj = []
isMouseDown = False
toolbarColor = "#3b3b3b"
titleColor = "#ffffff"

class modify:
    def update_title(title):
        titleLabelObj["text"] = title


def changePosition(windowObject, x, y):
    windowObject.geometry("+%s+%s" % (x, y))

def SCOSApp(title=__name__, width=640, height=360, fullscreen=False):
    global appObj, toolbarBgObj, titleLabelObj
    thisApp = Tk()
    thisApp.title(title)
    changePosition(thisApp, 100, 200)
    if fullscreen:
        thisApp.overrideredirect(0)
        thisApp.attributes("-fullscreen", True)
        thisApp.attributes("-zoomed", True)
        width, height = thisApp.winfo_screenwidth(), thisApp.winfo_screenheight()
    else:
        thisApp.geometry("%sx%s" % (width, height + 30)) # set width and height accordingly based on what main wants + what we need for toolbar
        thisApp.overrideredirect(1)



    def closeApp():
        thisApp.destroy()

    def allowDragApp(event):
        isDragButtonPressed = True

    def dragApp(event):
        if event.y <= height - abs(30 - height):
            thisApp.geometry("+%s+%s" % (round(thisApp.winfo_pointerx() - width / 2), round(thisApp.winfo_pointery() - 15)))

    toolbarBg = Canvas(thisApp, bg=toolbarColor, width=width+10, height=30)
    toolbarBg.place(anchor="nw")
    titleLabel = Label(thisApp, text=title, bg=toolbarColor, fg=titleColor)
    titleLabel.place(relx=0.01,rely=0.01,anchor="nw")
    Button(thisApp, text="x", command=closeApp).place(relx=1, anchor="ne") # button to close the app
    
    # dragBtn.place(relx=0.5, rely=0.01, anchor="n")
    thisApp.bind("<B1-Motion>", dragApp)
    # thisApp.bind_all("<ButtonRelease-1>", releaseDragApp)

    # save all important objects to global variables
    appObj = thisApp
    toolbarBgObj = toolbarBg
    titleLabelObj = titleLabel
    return thisApp
