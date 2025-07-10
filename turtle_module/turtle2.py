import turtle

wn = turtle.Screen()

jamal = turtle.Turtle()
tina = turtle.Turtle()

jamal.pencolor("blue")
jamal.pensize(5)

tina.pencolor("orange")
tina.pensize(5)

jamal.right(90)
jamal.forward(100)

tina.left(180)
tina.forward(50)

jamal.left(90)
jamal.forward(50)


wn.exitonclick()
