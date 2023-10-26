from tkinter import *
from tkinter import messagebox
import random

real_word = [
    "apple",
    "ball",
    "cat",
    "dog",
    "elephant",
    "fish",
    "girl",
    "horse",
    "ink",
    "jug",
    "kite",
    "lion",
    "mango",
    "nose",
    "orange",
    "parrot",
    "oueen",
    "rain",
    "sun",
    "tiger",
    "uniform",
    "voilet",
    "watch",
    "x-ray",
    "yellow",
    "zebra"
]

jumbled_word = [
    "palpe",
    "lbal",
    "atc",
    "ogd",
    "phaelent",
    "ifsh",
    "ligr",
    "orshe",
    "kni",
    "ugj",
    "tike",
    "oiln",
    "goman",
    "seno",
    "georan",
    "rarpto",
    "eqeun",
    "iran",
    "nus",
    "rtgie",
    "moufnir",
    "tvloei",
    "twcha",
    "yra-x",
    "lyloew",
    "bzrae"
]

options = random.randrange(0, len(jumbled_word), 1)


def one():
    global jumbled_word, real_word, options
    lbl2.config(text=jumbled_word[options])


def answer():
    global jumbled_word, real_word, options
    options = random.randrange(0, len(jumbled_word), 1)
    lbl1.config(text=jumbled_word[option])
    e1.delete(0, END)


def correct():
    global jumbled_word, real_word, options
    one_var = e1.get()
    if one_var == real_word[options]:
        messagebox.showinfo("Hurray!! you got it right")
        answer()
    else:
        messagebox.showinfo("Oops!! try better next time")
        e1.delete(0, END)


window = Tk()
window.geometry("350x400")
window.title("jumble word game")
window.configure(background="fuchsia")
lbl2 = Label(window, text=jumbled_word[options], font=("Arial", 25), bg="blue", fg="white")
lbl2.pack(pady=30, ipady=10, ipadx=10)
lbl1 = Label(window, text="write here", font=("Arial", 25), bg="blue", fg="white")
lbl1.pack(pady=30, ipady=10, ipadx=10)



correct_1 = StringVar()
e1 = Entry(window, font=("Arial", 25, "bold"), textvariable=correct_1)
e1.pack(ipady=5, ipadx=5)
correct_button = Button(window, text="click", font=("Arial", 20, "bold"), width=20, bg="red", fg="white", relief=GROOVE, command=correct)
correct_button.pack(pady=40)
reset_button = Button(window, text="reset", font=("Arial", 20, "bold"), width=20, bg="purple", fg="white", relief=GROOVE, command=answer)
reset_button.pack()
window.mainloop()


