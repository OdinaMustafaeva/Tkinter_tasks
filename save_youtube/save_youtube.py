from pytube import YouTube
import tkinter as tk
from tkinter import Label, Button, Radiobutton, Text, Entry, ttk, messagebox

wn = tk.Tk()
wn.geometry("400x300")
wn.configure(background='red')
wn.title("Save youtube")

# text
label_lotin = Label(wn, text="Save youtube", fg='white', bg='red', font=('Helvetica bold', 20))
label_lotin.pack(pady=30, padx=110)

#  text
label_text_ = Label(wn, text="Enter link http:/....", fg='white', bg='red', font=('Helvetica bold', 10))
label_text_.pack()

# text entry
entry_text_ = Entry(wn, font=(40))
entry_text_.pack(pady=20)


# label only funk
def my_label_traslate():
    try:
        YouTube(f"{entry_text_.get()}").streams.first().download()
        yt = YouTube(F"{entry_text_.get()}")
        yt.streams
    except Exception:
        messagebox.showerror("not found", "this link not found")
    else:
        label_tran_pink = Label(wn, text="Successful", width=20)
        label_tran_pink.pack(side=tk.RIGHT, padx=50)


# button text
button_fin_pink = Button(wn, text="Go", width=8, bg='green', fg='white', borderwidth=3,
                         command=my_label_traslate)
button_fin_pink.pack(side=tk.LEFT, padx=50)

if __name__ == '__main__':
    wn.mainloop()
