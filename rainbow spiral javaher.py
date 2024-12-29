import turtle

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Rainbow Spiral")
    turtle.speed(0)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for i in range(360):  # Draw 360 segments
        turtle.color(colors[i % len(colors)])
        turtle.width(i // 100 + 1)  # Gradually increase the width
        turtle.forward(i * 2 / 3)
        turtle.left(59)  # Create a spiral effect

    turtle.hideturtle()
    screen.mainloop()

# Call the function to draw the spiral
draw_spiral()