import turtle
import tkinter
from turtle import *
screen = turtle.Screen()
screen.bgcolor("red")
screen.title("SIX MINUS ONE - Learn Shapes")
turtle.shape('arrow')
turtle.pensize(6)

user_input= turtle.textinput("Shapes", "Type The Name Of Shape You Wanna Draw")
user_input= user_input.lower()

def triangle():
    for i in range(3):
        turtle.left(360/3)
        turtle.forward(199)
    turtle.hideturtle()

def square():
    for i in range(4):
        turtle.forward(199)
        turtle.right(360/4)
    turtle.hideturtle()

def rectangle():
    for i in range(2):
        turtle.forward(199)
        turtle.right(360/4)
        turtle.forward(99)
        turtle.right(360/4)
    turtle.hideturtle()

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def heart():
    turtle.speed(999)
    turtle.left(140)
    turtle.forward(113)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(112)
    turtle.hideturtle()

def pentagon():
    for i in range(5):
        turtle.left(360/5)
        turtle.forward(149)
    turtle.hideturtle()

def hexagon():
    for i in range(6):
        turtle.left(360/6)
        turtle.forward(149)
    turtle.hideturtle()

def heptagon():
    for i in range(7):
        turtle.left(360/7)
        turtle.forward(129)
    turtle.hideturtle()

def octagon():
    for i in range(8):
        turtle.left(360/8)
        turtle.forward(115)
    turtle.hideturtle()

def nonagon():
    for i in range(9):
        turtle.left(360/9)
        turtle.forward(97)
    turtle.hideturtle()

def decagon():
    for i in range(10):
        turtle.left(360/10)
        turtle.forward(79)
    turtle.hideturtle()

def star():
    for i in range(5):
        turtle.left(144)
        turtle.forward(199)
    turtle.hideturtle()

def spiral():
    turtle.speed(129)
    for i in range(130):
        turtle.forward(1+i)
        turtle.right(20)
    turtle.hideturtle()

def spiralsquare():
    turtle.speed(199)
    turtle.pensize(1)
    n = 200
    for i in range(100):
        turtle.left(360/4)
        turtle.forward(n)
        n-=2
    turtle.hideturtle()

def error():
    turtle.write('THE INPUT YOU ENTERED HAS NO SHAPE!!!', align='center')
    turtle.hideturtle()

def error2():
    turtle.write('ENTER SOMETHING!!!', align='center')
    turtle.hideturtle()

if user_input == "triangle":
    screen.title("TRIANGLE")
    triangle()
elif user_input == "square":
    screen.title("SQUARE")
    square()
elif user_input == "rectangle":
    screen.title("RECTANGLE")
    rectangle()
elif user_input == "circle":
    screen.title("CIRCLE")
    turtle.circle(50)
elif user_input == "pentagon":
    screen.title("PENTAGON")
    pentagon()
elif user_input == "hexagon":
    screen.title("HEXAGON")
    hexagon()
elif user_input == "heptagon":
    screen.title("HEPTAGON")
    heptagon()
elif user_input == "octagon":
    screen.title("OCTAGON")
    octagon()
elif user_input == "nonagon" or user_input == "nonane":
    screen.title("NONAGON")
    nonagon()
elif user_input == "decagon" or user_input == "decane":
    screen.title("DECAGON")
    decagon()
elif user_input == "star":
    screen.title("STAR")
    star()
elif user_input == "heart":
    screen.title("HEART")
    heart()
elif user_input == "spiral":
    screen.title("SPIRAL")
    spiral()
elif user_input == "spiralsquare" or user_input == "spiral square":
    screen.title("SPIRAL SQUARE")
    spiralsquare()
elif user_input == "":
    screen.title("ERROR")
    error2()
else:
    screen.title("ERROR")
    error()
turtle.done()
