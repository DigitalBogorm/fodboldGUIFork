# importing tkinter module
from tkinter import *
from tkinter.ttk import * #progressbar
#TODO: save functionality. Derudover, giver det mig også mulighed for at importere Dict'et
import pickle

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass

#TODO: importer pickle-kode fra tidligere opgave
filename = 'betalinger.pk'
fodboldtur = {}



class mainWindow:
    def __init__(self):
        #TODO: for at få noget som helst til at virke, skal det her være et dictionary eller en liste. Koden modificeres
        # til at tælle listen sammen i stedet
        self.total = countPayments()
        self.target = 4500

        # creating tkinter window
        self.root = Tk()

        #TEXT

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        closeButton = Button(self.root, text="save & close", command=lambda: closeAndSave())
        closeButton.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop

        mainloop()

#TODO: pickle-kode fra tidligere opgave
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

#TODO: funktionen her tæller alle indbetalinger sammen
def countPayments():
    pay = 0
    for i in fodboldtur:
        pay += fodboldtur[i]
    return(pay)

#Et desperat forsøg på at tvinge lukkeren til at gemme ændringer i 'fodboldtur'.
def addPayment(name, amount):
    fodboldtur[name] += amount

#TODO: Endnu en gang har jeg bare brugt en funktion fra den originale opgave, for at gemme ændringer og lukke filen
def closeAndSave():
    #Af årsager jeg ikke lige kan regne ud, gemmer den ikke. Den lader til at ignorere enhver ændring i fodboldtur,
    #og gemmer bare det originale dictionary, i stedet for den opdaterede version. Ikke værd at spilde mere tid på.
    print(fodboldtur)
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    quit()

if __name__ == '__main__':
    main = mainWindow()

