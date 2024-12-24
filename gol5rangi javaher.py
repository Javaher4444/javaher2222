import turtle

screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)

def draw_petals(color):
    flower.color(color)
    flower.begin_fill()
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)
    flower.end_fill()

colors = ["red", "yellow", "blue", "green", "purple"]

for color in colors:
    draw_petals(color)
    flower.left(72)

flower.hideturtle()

turtle.done()