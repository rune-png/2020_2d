import tkinter as tk

class Program2(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        #Her oprettes en række widgets til vores brugerflade
        lbl1 = tk.Label(self, text = "Navn")
        lbl2 = tk.Label(self, text = "Alder")

        #Et tekstfelt hedder "Entry" i tkinter
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        button1 = tk.Button(self, text="Tilføj", command = self.button1_action)

        #Radiobuttons hænger sammen via en fælles variabel
        self.gender_var = tk.IntVar()
        self.gender_var.set(1)
        radio1 = tk.Radiobutton(self, text="Mand", variable = self.gender_var, value = 1)
        radio2 = tk.Radiobutton(self, text="Kvinde", variable = self.gender_var, value = 2)

        #Et større område med flere linjers tekst hedder bare "Text"
        self.textarea1 = tk.Text(self)

        #I stedet for "pack" bruger vi har "grid"
        #For hver widget skal vi angive hvilken række og kolonne
        #de skal placeres i.
        lbl1.grid(row = 0, column = 0)
        self.entry1.grid(row = 0, column = 1)
        lbl2.grid(row = 1, column = 0)
        self.entry2.grid(row = 1, column = 1)
        radio1.grid(row=2, column = 0)
        radio2.grid(row=2, column = 1)
        button1.grid(row = 3, column = 0, columnspan = 2)
        #Læg mærke til vores textarea, der skal dække to kolonner:
        self.textarea1.grid(row = 4, column = 0, columnspan = 2)

        self.pack()

    def button1_action(self):
        #Med funktionen get() hentes teksten fra et tekstfelt.
        name = self.entry1.get()
        if self.gender_var.get() == 1:
            gender = "mand"
        else:
            gender = "kvinde"
        self.textarea1.insert(tk.END, "{} er en {}\n".format(name, gender))


root = tk.Tk()

prg = Program2()
prg.master.title('Eksempel 2')
prg.mainloop()

#Opgaver:

#Funktionen button1_action bruger slet ikke det tekstfelt, der hedder "entry2"
#Tilføj personens alder til den tekst, der skrives i tekstfeltet.

#På denne side kan du finde lidt mere information om Text-widget.
#Den har mange muligheder for at vise teksten på forskellige måder:
# https://www.python-course.eu/tkinter_text_widget.php
