import tkinter as tk
from tkinter import Label, Button, Radiobutton, Text, Entry, ttk
from datetime import datetime
from translate import Translator

wn = tk.Tk()
wn.geometry("400x400")
wn.configure(background='pink')
wn.title("Pink translate")

# PINK Translate text
label_pink = Label(wn, text="Pink Translate", fg='black', bg='pink', font=('Helvetica bold', 20))
label_pink.pack(pady=30, padx=110)

# label text
label_text_pink = Label(wn, text="Enter text", fg='yellow', bg='pink', font=('Helvetica bold', 10))
label_text_pink.pack()

# text entry
entry_text_pink = Entry(wn, font=(40))
entry_text_pink.pack(pady=20)

# language text
label_lang_text_pink = Label(wn, text="Enter language", fg='yellow', bg='pink', font=('Helvetica bold', 10))
label_lang_text_pink.pack(pady=10, padx=0)

# combobox 5 language
combobox_pink = ttk.Combobox(wn, values=['uz', 'tk', "uz", "ug", "ko"], width=5)
combobox_pink.pack()


# label only funk
def my_label_traslate():
    trant = Translator(to_lang=str(combobox_pink.get()))
    lis = trant.translate(entry_text_pink.get())
    label_tran_pink = Label(wn, text=f'{lis}', width=20)
    label_tran_pink.pack(side=tk.RIGHT, padx=50)
    with open("history.csv", "a") as file:
        file.write(f"\n{entry_text_pink.get()},{combobox_pink.get()},{datetime.now()}")


# button text
button_fin_pink = Button(wn, text="Go", width=8, bg='yellow', fg='black', borderwidth=3,
                         command=my_label_traslate)
button_fin_pink.pack(side=tk.LEFT, padx=50)

if __name__ == '__main__':
    wn.mainloop()
