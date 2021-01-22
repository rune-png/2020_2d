
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class Opg1(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.build_gui()



    def handle(self):
        t = self.entry.get()
        if len(t) == 0:
            messagebox.showinfo(title="Fejl i input", message="Du skal skrive noget")
        else:
            messagebox.showinfo(title="Fint", message="Du skrev noget!")


    def build_gui(self):
        self.entry = ttk.Entry(self, text="")
        self.but = ttk.Button(self, text="Klar", command=self.handle)
        self.label = ttk.Label(self, text="Skriv noget:")

        self.label.pack(padx=10, pady=10)
        self.entry.pack(padx=10, pady=10)
        self.but.pack(padx=10, pady=10)

        self.pack()



root = tk.Tk()

prg = Opg1()
prg.master.title('Input')
prg.mainloop()
