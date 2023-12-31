import turtle
import tkinter
import textwrap
from tkinter import messagebox as mb
from tkinter import *
import wikipedia as wiki
screen = turtle.Screen()
screen.bgcolor("#ADD8E6")
screen.title("SIX MINUS ONE - The Encyclopedia: The Flora")
screen.addshape("images/flora.gif")
turtle.shape("images/flora.gif")
turtle.penup()
turtle.goto(0,180)
img = tkinter.Image("photo", file="images/logo.png")
turtle._Screen._root.iconphoto(True, img)
mb.showwarning("Warning", "Please avoid typing a scientific name")

u_input = turtle.textinput("The Encyclopedia ", "Type the name of Flora")
user_input= u_input.lower().replace(" ","")

def sunflower():
    def sunfloweri():
        sc= Tk()
        sc.title("Learn about Sunflower")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("sunflower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#f4c2c2')
        text.insert(INSERT, A1)
        text.pack()
        bt = Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/sunflower.gif")
    turtle.shape("images/sunflower.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(sunfloweri())

def lily():
    def lilyi():
        sc= Tk()
        sc.title("Learn about Lily")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("lily flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FEFF86')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/lily.gif")
    turtle.shape("images/lily.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(lilyi())

def bluerose():
    def bluerosei():
        sc= Tk()
        sc.title("Learn about Blue Rose")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("blue rose flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#C2DE9E')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/blue rose.gif")
    turtle.shape("images/blue rose.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(bluerosei())

def callalily():
    def callalilyi():
        sc= Tk()
        sc.title("Learn about Calla Lily")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("Arum lily", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FFE5B4')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/calla lily.gif")
    turtle.shape("images/calla lily.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(callalilyi())

def carnation():
    def carnationi():
        sc= Tk()
        sc.title("Learn about Carnation")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("carnation flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FFFDD0')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/carnation.gif")
    turtle.shape("images/carnation.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(carnationi())

def chrysanthemums():
    def chrysanthemumsi():
        sc= Tk()
        sc.title("Learn about Chrysanthemums")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("chrysanthemums flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FADADD')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/chrysanthemums.gif")
    turtle.shape("images/chrysanthemums.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(chrysanthemumsi())

def daffodil():
    def daffodili():
        sc= Tk()
        sc.title("Learn about Daffodil")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("daffodil flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#E4CBF5')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/daffodil.gif")
    turtle.shape("images/daffodil.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(daffodili())

def daisy():
    def daisyi():
        sc= Tk()
        sc.title("Learn about Daisy")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("common daisy flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#B1FADF')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/daisy.gif")
    turtle.shape("images/daisy.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(daisyi())

def hibiscus():
    def hibiscusi():
        sc= Tk()
        sc.title("Learn about Hibiscus")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("hibiscus flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#F4C2C2')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/hibiscus.gif")
    turtle.shape("images/hibiscus.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(hibiscusi())

def hyacinth():
    def hyacinthi():
        sc= Tk()
        sc.title("Learn about Hyacinth")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("hyacinth flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#C2DE9E')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/hyacinth.gif")
    turtle.shape("images/hyacinth.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(hyacinthi())

def iris():
    def irisi():
        sc= Tk()
        sc.title("Learn about Iris")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("iris flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FFE5B4')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/iris.gif")
    turtle.shape("images/iris.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(irisi())

def lilac():
    def lilaci():
        sc= Tk()
        sc.title("Learn about Lilac")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("syringa", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FFFDD0')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/lilac.gif")
    turtle.shape("images/lilac.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(lilaci())

def lotus():
    def lotusi():
        sc= Tk()
        sc.title("Learn about Lotus")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("lotus flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FADADD')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/lotus.gif")
    turtle.shape("images/lotus.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(lotusi())

def orchid():
    def orchidi():
        sc= Tk()
        sc.title("Learn about Orchid")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("orchidaceae", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#E4CBF5')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/orchid.gif")
    turtle.shape("images/orchid.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(orchidi())

def pansy():
    def pansyi():
        sc= Tk()
        sc.title("Learn about Pansy")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("pansy flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#B1FADF')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/pansy.gif")
    turtle.shape("images/pansy.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(pansyi())

def peruvianlily():
    def peruvianlilyi():
        sc= Tk()
        sc.title("Learn about Peruvian Lily")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("alstroemeria", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FEFF86')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/peruvian lily.gif")
    turtle.shape("images/peruvian lily.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(peruvianlilyi())

def petunia():
    def petuniai():
        sc= Tk()
        sc.title("Learn about Petunia")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("petunia flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#F4C2C2')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/petunia.gif")
    turtle.shape("images/petunia.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(petuniai())

def pitcherplant():
    def pitcherplanti():
        sc= Tk()
        sc.title("Learn about Pitcher Plant")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("nepenthes", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#C2DE9E')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/pitcher plant.gif")
    turtle.shape("images/pitcher plant.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(pitcherplanti())

def rose():
    def rosei():
        sc= Tk()
        sc.title("Learn about Rose")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("rose flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FFE5B4')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/rose.gif")
    turtle.shape("images/rose.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(rosei())

def tulip():
    def tulipi():
        sc= Tk()
        sc.title("Learn about Tulip")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("tulip flower", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FFFDD0')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/tulip.gif")
    turtle.shape("images/tulip.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(tulipi())

def venusflytrap():
    def venusflytrapi():
        sc= Tk()
        sc.title("Learn about Venus Flytrap")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A =  wiki.summary("venus flytrap", sentences=4)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#FADADD')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/venus flytrap.gif")
    turtle.shape("images/venus flytrap.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(venusflytrapi())

def whiterose():
    def whiterosei():
        sc= Tk()
        sc.title("Learn about White Rose")
        sc.geometry("743x453")
        source = Label(sc, text="Source: Wikipedia")
        source.config(font=("Courier",10))
        source.pack()
        A_ =  wiki.summary("Rosa", sentences=4)
        A = "White rose is a specie of Rosa family. " + str(A_)
        A1 = '\n'.join(textwrap.wrap(A, 80))
        text= Text(sc, bg='#E4CBF5')
        text.insert(INSERT, A1)
        text.pack()
        Button(sc, text= "OK & Exit", command=sc.destroy).pack()
        sc.mainloop()
    turtle.goto(0,120)
    turtle.addshape("images/white rose.gif")
    turtle.shape("images/white rose.gif")
    screen.tracer(0)
    turtle.penup()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-50, -200)
    turtle.goto(-50 + 130, -200)
    turtle.goto(-50 + 130, -200 + 50)
    turtle.goto(-50, -200 + 50)
    turtle.goto(-50, -200)
    turtle.end_fill()
    turtle.goto(-50 + 15, -200 + 15)
    turtle.write("Learn More", font = ('Arial', 15, 'normal'))
    screen.onclick(whiterosei())

def florascreen():
    wn = Tk()
    wn.title("The Encyclopedia: The Flora")
    wn.geometry("400x150")
    wn.configure(bg = "#FFE0A6")
    Button(wn, text = "Sunflower", fg = "red", command = sunflower).grid(column=0, row=1)
    Button(wn, text = "Lily", fg = "blue",command = lily).grid(column=0, row=2)
    Button(wn, text = "Blue Rose", fg = "lime", command = bluerose).grid(column=0, row=3)
    Button(wn, text = "Calla Lily", fg = "brown", command = callalily).grid(column=0, row=4)
    Button(wn, text = "Carnation", fg = "gold", command = carnation).grid(column=0, row=5)
    Button(wn, text = "Chrysanthemums", fg = "lime", command = chrysanthemums).grid(column=1, row=1)
    Button(wn, text = "Daffodil", fg = "purple", command = daffodil).grid(column=1, row=2)
    Button(wn, text = "Daisy", fg = "indigo", command = daisy).grid(column=1, row=3)
    Button(wn, text = "Hibiscus", fg = "dark blue", command = hibiscus).grid(column=1, row=4)
    Button(wn, text = "Hyacinth", fg = "orange", command = hyacinth).grid(column=1, row=5)
    Button(wn, text = "Iris", fg = "midnight blue", command = iris).grid(column=2, row=1)
    Button(wn, text = "Lilac", fg = "cyan", command = lilac).grid(column=2, row=2)
    Button(wn, text = "Lotus", fg = "navy blue", command = lotus).grid(column=2, row=3)
    Button(wn, text = "Orchid", fg = "blue", command = orchid).grid(column=2, row=4)
    Button(wn, text = "Pansy", fg = "brown", command = pansy).grid(column=2, row=5)
    Button(wn, text = "Peruvian Lily", fg = "red", command = peruvianlily).grid(column=3, row=1)
    Button(wn, text = "Petunia", fg = "lime", command = petunia).grid(column=3, row=2)
    Button(wn, text = "Pitcher Plant", fg = "cyan", command = pitcherplant).grid(column=3, row=3)
    Button(wn, text = "Rose", fg = "green", command = rose).grid(column=3, row=4)
    Button(wn, text = "Tulip", fg = "indigo", command = tulip).grid(column=3, row=5)
    Button(wn, text = "Venus Flytrap", fg = "orange", command = venusflytrap).grid(column=4, row=1)
    Button(wn, text = "White Rose", fg = "black", command = whiterose).grid(column=4, row=2)
    Button(wn, text= "OK & Exit", bg = "red", command=wn.destroy).grid(column=4, row=5)
    wn.mainloop()

def message():
    sc= Tk()
    sc.title("Message")
    sc.geometry("250x140")
    err_mess = Label(sc, text="Application closed")
    err_mess.config(font=("Courier",10))
    err_mess.pack()
    text= Text(sc, height= 5, width =100, bg='#D9D4D4')
    A = "Thanks for having us!!!"
    A1 = '\n'.join(textwrap.wrap(A,30))
    text.insert(INSERT, A1)
    text.pack()
    Button(sc, text= "OK & Exit", command=sc.destroy).pack()
    sc.mainloop()

def error():
    sc= Tk()
    sc.title("ERROR")
    sc.geometry("250x140")
    err_mess = Label(sc, text="Error occurred")
    err_mess.config(font=("Courier",10))
    err_mess.pack()
    text= Text(sc, height= 5, width =100, bg='#D9D4D4')
    A = "You have to enter some input!!!"
    A1 = '\n'.join(textwrap.wrap(A,30))
    text.insert(INSERT, A1)
    text.pack()
    Button(sc, text= "OK & Exit", command=sc.destroy).pack()
    sc.mainloop()

lst_flora = ["bluerose","callalily","carnation","chrysanthemums","daffodil","daisy","hibiscus","hyacinth","iris","lilac","lily","lotus","orchid","pansy","peruvianlily","petunia","pitcherplant","rose","sunflower","tulip","venusflytrap","whiterose","flora"]

if user_input == "flora":
    florascreen()
if user_input == "sunflower":
    sunflower()
if user_input == "lily" or user_input == "lilium":
    lily()
if user_input == "bluerose":
    bluerose()
if user_input == "callalily":
    callalily()
if user_input == "carnation":
    carnation()
if user_input == "chrysanthemums":
    chrysanthemums()
if user_input == "daffodil":
    daffodil()
if user_input == "daisy":
    daisy()
if user_input == "hibiscus":
    hibiscus()
if user_input == "hyacinth":
    hyacinth()
if user_input == "iris":
    iris()
if user_input == "lilac":
    lilac()
if user_input == "lotus":
    lotus()
if user_input == "orchid":
    orchid()
if user_input == "pansy":
    pansy()
if user_input == "peruvianlily":
    peruvianlily()
if user_input == "pitcherplant":
    pitcherplant()
if user_input == "venusflytrap":
    venusflytrap()
if user_input == "whiterose":
    whiterose()
if user_input == "petunia":
    petunia()
if user_input == "rose":
    rose()
if user_input == "tulip":
    tulip()
if user_input == "":
    error()
if user_input not in lst_flora:
    screen.tracer(0)
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(-120,-20)
    turtle.goto(-120 + 250, -20)
    turtle.goto(-120 + 250, -20 + 50)
    turtle.goto(-120, -20 + 50)
    turtle.goto(-120, -20)
    turtle.end_fill()
    turtle.goto(-115,0)
    turtle.write("We don't have that entry in our encyclopedia yet!!!", font = ('Arial', 8, 'normal'))
else:
    message()

screen.mainloop()
turtle.done()
