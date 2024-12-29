import turtle

def draw_heart():
    screen = turtle.Screen()
    screen.bgcolor("green")
    screen.title("Heart Shape")
    turtle.speed(5)

    turtle.color("blue")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

    turtle.hideturtle()
    screen.mainloop()

# Call the function to draw the heart
draw_heart()