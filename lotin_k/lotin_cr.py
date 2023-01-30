from lotin import transliterate
import tkinter as tk
from tkinter import Label, Button, Radiobutton, Text, Entry, ttk


wn = tk.Tk()
wn.geometry("400x300")
wn.configure(background='lime')
wn.title("LOTIN KERIL")

#  lotin text
label_lotin = Label(wn, text="Lotin keril", fg='black', bg='lime', font=('Helvetica bold', 20))
label_lotin.pack(pady=30, padx=110)

# label text
label_text_ = Label(wn, text="Enter text", fg='blue', bg='lime', font=('Helvetica bold', 10))
label_text_.pack()

# text entry
entry_text_ = Entry(wn, font=(40))
entry_text_.pack(pady=20)


# label only funk
def my_label_traslate():
    b = transliterate(entry_text_.get(), "cyrillic")
    label_tran_pink = Label(wn, text=f'{b}', width=20)
    label_tran_pink.pack(side=tk.RIGHT, padx=50)


# button text
button_fin_pink = Button(wn, text="Go", width=8, bg='yellow', fg='black', borderwidth=3,
                         command=my_label_traslate)
button_fin_pink.pack(side=tk.LEFT, padx=50)

if __name__ == '__main__':
    wn.mainloop()
