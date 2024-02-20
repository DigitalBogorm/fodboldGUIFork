    # importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow



class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()

        #TODO: Erstat billedet med en (nogenlunde) dynamisk liste over navne
        #img = ImageTk.PhotoImage(Image.open("assets/img/cyl.png"))
        #panel = Label(self.listWindow, image=img)
        #panel.image = img
        #panel.pack(side="bottom", fill="both", expand="yes")

        #Fodboldtur importeres først hernede, for at undgå problemer med cirkulær importering
        from main import fodboldtur
        dictKeys = list(fodboldtur.keys())
        #Mit 'for'-loop opfører sig lidt underligt (formentligt pga. brugen af lister), så jeg bruger loopCounteren til
        #at måle, hvor mange gange den faktisk har kørt
        loopCounter = 0
        for i in dictKeys:
            txt = str((str(dictKeys[loopCounter]), str(fodboldtur[dictKeys[loopCounter]])))
            Label(self.listWindow, text=txt).pack()
            loopCounter += 1