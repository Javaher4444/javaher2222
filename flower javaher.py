import turtle

turtle.fillcolor('red')
turtle.begin_fill()
for i in range(5):
    turtle.circle(30, 180)
    turtle.right(108)
turtle.end_fill()

turtle.up()
turtle.goto(-40, 28)
turtle.down()

turtle.color('yellow')
turtle.dot(50)

turtle.done()
