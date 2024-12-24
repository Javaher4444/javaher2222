import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Night Sky with Stars and Moon")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

def draw_moon():
    pen.penup()
    pen.goto(200, 100)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

def draw_half_moon():
    pen.penup()
    pen.goto(225, 125)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

for _ in range(24):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    size = random.randint(10, 20)
    draw_star(x, y, size)

draw_moon()
draw_half_moon()

screen.mainloop()