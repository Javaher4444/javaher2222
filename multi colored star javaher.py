import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colorful Star")
    turtle.speed(8)

    colors = ["red", "yellow", "green", "blue", "purple"]

    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()

    for i in range(50):  # Create the star with 50 lines
        turtle.color(colors[i % len(colors)])
        turtle.forward(200)
        turtle.left(123)  # Star angle to make it geometric

    turtle.hideturtle()
    screen.mainloop()

# Call the function to draw the star
draw_star()
