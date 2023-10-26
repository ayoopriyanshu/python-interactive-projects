import tkinter
import turtle
import textwrap
from turtle import *
from tkinter import *
import os
wn = tkinter.Tk()
wn.title("Welcome to SIX MINUS ONE")
wn.configure(bg = "#FA7268")
wn.geometry("600x400")
logoimg = PhotoImage(file= "images/logo.png")
wn.iconphoto(True,logoimg)
image = PhotoImage(file = "images/main.png")
label = Label(image=image)
label.pack()
label2 = Label(wn, text="Choose any one of our creations.", font=("San Francisco",15,"bold"), bg ="blue", fg = "yellow")
label2.place(x=160,y=225)
def shapes():
    os.system("Shapes101.py")
def encyco():
    os.system("Flora101.py")
def jumble():
    os.system("jumble.py")
def Tic():
    os.system("tictactoe.py")
def ping():
    os.system("pingpong.py")
def guesscolor():
    os.system("GuessTheColour.py")
def credit():
    sc= Tk()
    sc.title("Credits")
    sc.geometry("425x175")
    hd = Label(sc, text="SIX MINUS ONE: Credits")
    hd.config(font=("San Francisco",10))
    hd.pack()
    text= Text(sc, height= 7, width =100, bg='#D9D4D4')
    A1  = "JUMBLE: Gayatri Purohit(E21CSEU0946)                "
    A2  = "TIC TAC TOE: Tarush Singh(E21CSEU0974)              "
    A3  = "COLOUR GUESSOR: Hardik Jain(E21CSEU0973)            "
    A4  = "PING PONG: Sparsh Saria(E21EPYU0006)                "
    A5  = "FLORA ENCYCLOPEDIA: Priyanshu Sharma(E21CSEU0955)   "
    A6  = "SHAPES LEARNING: Priyanshu Sharma(E21CSEU0955)      "
    text.insert(INSERT, A1)
    text.insert(INSERT, A2)
    text.insert(INSERT, A3)
    text.insert(INSERT, A4)
    text.insert(INSERT, A5)
    text.insert(INSERT, A6)
    text.pack()
    Button(sc, text= "Close", command=sc.destroy).pack()
    sc.mainloop()
Bu1 = tkinter.Button(wn, text = "Shapes Learning", fg = "red", command = shapes)
Bu2 = tkinter.Button(wn, text = "Flora Encyclopedia", fg = "blue", command = encyco)
Bu3 = tkinter.Button(wn, text = "Jumble", fg = "red", command = jumble)
Bu4 = tkinter.Button(wn, text = "Tic Tac Toe", fg = "blue", command = Tic)
Bu5 = tkinter.Button(wn, text = "Ping Pong", fg = "red", command = ping)
Bu6 = tkinter.Button(wn, text = "Colour Guessor", fg = "blue", command = guesscolor)
Bu7 = tkinter.Button(wn, text = "Exit", bg = "red", command = wn.destroy).place(x= 570, y=375)
Bu8 = tkinter.Button(wn, text = "Credits", bg = "#d4af37", command = credit).place(x=520, y=375)
Bu1.place(x=35,y=300)
Bu2.place(x=175,y=300)
Bu3.place(x=320,y=300)
Bu4.place(x=400,y=300)
Bu5.place(x=500,y=300)
Bu6.place(x=255,y=350)
wn.mainloop()
