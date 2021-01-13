import tkinter as tk
 
def bmi_regner(height, weight):  
    return(weight)/((height/100.0)**2)

class opg(tk.Frame):
    def UPDATEBMI(self, value):
        self.result.configure(text=bmi_regner(self.height.get(), self.weight.get()))
    def __init__(self):
        tk.Frame.__init__(self)

        self.height = tk.Scale(self, from_=120, to_=200, label=("Højde (cm)"), orient = "horizontal", command=self.UPDATEBMI)
        self.height.set(170)
        self.height.pack()

        self.weight = tk.Scale(self, from_=50, to_=200, label=("Vægt (Kg)"), orient="horizontal", command=self.UPDATEBMI)
        self.weight.set(60)
        self.weight.pack()

        self.result=tk.Label(self, text="Din bmi")
        self.result.pack()
        self.pack()


root = tk.Tk()

prg = opg()
prg.master.title('Eksempel 2')
prg.mainloop()