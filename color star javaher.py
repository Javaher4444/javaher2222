import turtle
t=turtle.Turtle()
t.fillcolor('blue')

t.begin_fill()

for _ in range(5):
    t.forward(300)
    t.right(144)

t.end_fill()
turtle.mainloop()

