# importing tkinter module
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,text="Indbetal").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        #TODO: Indsættelse af ekstra felt til registrering af navn. Nødvendigt for at kunne modificere dictionaryet
        from main import fodboldtur
        names = list(fodboldtur.keys())
        self.nameChoice = StringVar()
        self.nameChoice.set("Vælg dit navn fra menuen")

        self.nameInput = OptionMenu(self.payWindow, self.nameChoice, *names)
        self.nameInput.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

    def addMoney(self):
        from main import addPayment
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        addPayment(self.nameChoice.get(), amount)
        #Koden her får bare lov at være i fred, for at progresslabelen opdateres i realtime.
        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
