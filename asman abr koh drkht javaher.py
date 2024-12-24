import turtle

screen = turtle.Screen()
screen.bgcolor("sky blue")
screen.title("Mountain, Sun, Clouds, and Trees")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_mountain():
    pen.penup()
    pen.goto(-400, -100)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    pen.setheading(60)
    for _ in range(3):
        pen.forward(200)
        pen.right(120)
    pen.end_fill()

    pen.penup()
    pen.goto(-200, -100)
    pen.pendown()
    pen.setheading(60)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(200)
        pen.right(120)
    pen.end_fill()

    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.setheading(60)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(200)
        pen.right(120)
    pen.end_fill()

    pen.penup()
    pen.goto(200, -100)
    pen.pendown()
    pen.setheading(60)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(200)
        pen.right(120)
    pen.end_fill()

def draw_sun():
    pen.penup()
    pen.goto(200, 150)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

def draw_cloud(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.color("white")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    pen.penup()
    pen.goto(x + 40, y)
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    pen.penup()
    pen.goto(x + 20, y + 20)
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

def draw_tree(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    pen.setheading(0)
    for _ in range(2):
        pen.forward(10)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(x - 20, y + 30)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    pen.penup()
    pen.goto(x + 20, y + 30)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    pen.penup()
    pen.goto(x - 10, y + 50)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()

draw_mountain()
draw_sun()
draw_cloud(-150, 200)
draw_cloud(50, 250)
draw_cloud(200, 230)

draw_tree(-200, -170)
draw_tree(-100, -170)
draw_tree(0, -170)
draw_tree(100, -170)
draw_tree(200, -170)
draw_tree(300, -170)

screen.mainloop()