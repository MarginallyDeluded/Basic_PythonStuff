import turtle

wn = turtle.Screen()
wn.bgcolor("black")

vicious = turtle.Turtle()
vicious.pensize(3)
vicious.color("grey","orange")

vicious.begin_fill()

vicious.left(30)

for i in range(6):
    vicious.forward(100)
    vicious.right(60)

vicious.end_fill()
vicious.left(150)

vicious.color("grey","red")

for j in range(6):
    vicious.begin_fill()
    vicious.forward(100)
    vicious.left(90)
    vicious.forward(100)
    vicious.left(90)
    vicious.forward(100)
    vicious.end_fill()
    vicious.right(120)


wn.exitonclick()

