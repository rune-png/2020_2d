import tkinter as tk

class KnapProgram1(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        #Her oprettes en knap. Med argumentet "command" vælges hvilken
        #funktion, der skal udføres når man klikker på knappen.
        self.button1 = tk.Button(self, text = 'OK', command = self.knap1_action)
        #For at placere knappen på vores frame kaldes funktionen "pack"
        self.button1.pack(side=tk.TOP)

        #Og en label, så vi kan lave noget output når man klikker på knappen
        self.label1 = tk.Label(self, text = 'En label til tekst')
        self.label1.pack(side=tk.TOP)

        #Til sidst skal vores frame også "packes"
        self.pack()

    def knap1_action(self):
        self.label1.configure(text = "Du har klikket på knappen!")


root = tk.Tk()

prg = KnapProgram1()
prg.master.title('Eksempel 1')
prg.mainloop()

#Opgaver:
# Lav en ændring i funktionen "knap1_action",
# og vælg en anden tekst til knappen.

#Prøv at ændre i de linjer, hvor pack()-funktionen kaldes.
#Lav side=tk.TOP om til side=tk.BOTTOM, og se hvad resultatet bliver.

# Tilføj endnu en knap.
