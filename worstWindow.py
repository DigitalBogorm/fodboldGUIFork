# importing tkinter module
from tkinter import *
import operator

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")

        #TODO: Tilføj sortering og læsning af dict
        from main import fodboldtur
        #kode taget (og svagt modificeret) fra https://ioflood.com/blog/python-sort-dictionary-by-value/, bør skabe
        #en sorteret liste over værdier
        Sortering = dict(sorted(fodboldtur.items(), key=operator.itemgetter(1)))
        print(Sortering)
        keyList = list(Sortering.keys())
        print(keyList)
        navnList = [keyList[0], keyList[1], keyList[2]]
        del navnList[3:]
        print(navnList)

        #Hernede skrives de på listen
        loops = 0
        for i in navnList:
            txt = (str(navnList[loops]), " mangler at betale ", str(4500 - fodboldtur[navnList[loops]]))
            Label(self.worstWindow, text=txt).pack()
            loops += 1

