import turtle

color = ["red", "purple", "blue",
        "green", "orange", "yellow"]

cursor = turtle.Pen()

turtle.bgcolor("midnightblue")

for c in range(360):
     cursor.pencolor(color[c % 6])
     cursor.width(c/100 + 1)
     cursor.forward(c)
     cursor.left(59)
     