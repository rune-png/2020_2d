import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from notedata import NoteData

class NoteProgram(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.data = NoteData()

        self.build_gui()


    def delete_note(self):
        #Find den valgte note i treeview
        if messagebox.askyesno('Bekræft', 'Er du sikker på at du vil slette noten?'):
            curItem = self.note_grid.item(self.note_grid.focus())['values']
            if len(curItem) > 0:
                selected_date = curItem[0]
                self.data.delete_note(selected_date)
                self.update_grid()
        else:
            pass

    def on_note_selected(self, event):
        curItem = self.note_grid.item(self.note_grid.focus())['values']
        if len(curItem) > 0:
            self.lbl_date.configure(text="Dato: {}".format(curItem[0]))
            self.entry_cat.delete(0,tk.END)
            self.entry_cat.insert(0,curItem[1])
            self.ed_content.delete("1.0", tk.END)
            self.ed_content.insert(tk.END, curItem[2])


    def update_grid(self):
        notes = self.data.get_notes()
        self.note_grid.delete(*self.note_grid.get_children())
        for note in notes:
            self.note_grid.insert("", tk.END, values=(note['date'].strftime('%Y-%m-%d %H:%M:%S.%f'), note['category'], note['text']))

    def new_note(self):
        def insert():
            cat = cat_value.get()
            text = textNote.get("1.0",tk.END)
            self.data.add_note(text, cat)
            self.update_grid()
            dialog.destroy()
            dialog.update()

        def cancel():
            dialog.destroy()
            dialog.update()

        dialog = tk.Toplevel()

        lblKategori = tk.Label(dialog, text="Kategori")
        kategorier = self.data.get_categories()
        cat_value=tk.StringVar()
        cbKategori = ttk.Combobox(dialog, values = kategorier, textvariable=cat_value)

        lblNote = tk.Label(dialog, text="Note")
        textNote = tk.Text(dialog, height=4)

        butCancel = tk.Button(dialog, text="Annuller", command=cancel)
        butOK = tk.Button(dialog, text="OK", command=insert)

        lblKategori.grid(column = 0, row = 0)
        cbKategori.grid(column = 1, row = 0)
        lblNote.grid(column = 0, row = 1)
        textNote.grid(column = 1, row = 1, columnspan = 2)
        butCancel.grid(column = 1, row = 2, sticky=tk.W)
        butOK.grid(column = 2, row = 2, sticky=tk.W)


    def cancel_edit(self):
        pass
        #Genindlæs noten fra datalaget

    def save_note(self):
        pass
        #Gem ændringer i datalaget

    def build_gui(self):
        right_frame = tk.Frame(self)
        self.button_frame = tk.Frame(self)
        self.edit_frame = tk.Frame(right_frame)
        self.view_frame = tk.Frame(right_frame)

        self.edit_frame.pack(side=tk.TOP)
        self.view_frame.pack(side=tk.BOTTOM)
        self.button_frame.pack(side=tk.LEFT)
        right_frame.pack(side=tk.RIGHT)
        self.pack()

        # Button frame
        self.but_new = tk.Button(self.button_frame, text = "Ny note", command=self.new_note)
        self.but_delete = tk.Button(self.button_frame, text = "Slet note", command=self.delete_note)
        separator = ttk.Separator(self.button_frame, orient='horizontal')
        lbl_filter = tk.Label(self.button_frame, text = "Filter")

        self.but_new.pack(side=tk.TOP)
        self.but_delete.pack(side=tk.TOP)
        separator.pack(side=tk.TOP)
        lbl_filter.pack(side=tk.TOP)

        # Edit frame
        self.lbl_date = tk.Label(self.edit_frame, text = "Dato: ")
        self.lbl_cat = tk.Label(self.edit_frame, text = "Kategori: ")
        self.entry_cat = tk.Entry(self.edit_frame, text = "")
        self.ed_content = tk.Text(self.edit_frame, height=8)
        self.but_save = tk.Button(self.edit_frame, text = "Gem", command=self.save_note)
        self.but_cancel = tk.Button(self.edit_frame, text = "Fortryd", command=self.cancel_edit)

        self.lbl_date.grid(row = 0, column = 0, columnspan = 2)
        self.lbl_cat.grid(row = 1, column = 0)
        self.entry_cat.grid(row = 1, column = 1)
        self.ed_content.grid(row = 0, column = 2, columnspan=2, rowspan=4, padx=5, pady=5)
        self.but_save.grid(row = 2, column = 0, columnspan = 2)
        self.but_cancel.grid(row = 3, column = 0, columnspan = 2)

        self.note_grid = ttk.Treeview(self.view_frame, column=("columnDato", "columnKategori", "columnNote"), show='headings')
        self.note_grid.bind("<ButtonRelease-1>", self.on_note_selected)
        self.note_grid.heading("#1", text="Dato")
        self.note_grid.heading("#2", text="Kategori")
        self.note_grid.heading("#3", text="Note")
        self.note_grid["displaycolumns"]=("columnDato", "columnKategori", "columnNote")
        ysb = ttk.Scrollbar(self.view_frame, command=self.note_grid.yview, orient=tk.VERTICAL)
        self.note_grid.configure(yscrollcommand=ysb.set)
        self.note_grid.pack(side = tk.TOP)



root = tk.Tk()

prg = NoteProgram()
prg.master.title('Mine noter')
prg.mainloop()
