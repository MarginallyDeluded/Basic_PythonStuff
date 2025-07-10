import turtle

wn = turtle.Screen()

spike = turtle.Turtle()
ed = turtle.Turtle()
spike.pensize(5)
ed.pensize(5)

ed.pencolor("orange")
spike.pencolor("blue")

wn.bgcolor("green")


for i in range(4):
    spike.forward(100)
    spike.right(90)
    i = i+1

ed.right(180)
ed.forward(25)

for j in range(3):
    if j == 2:
        ed.right(120)
        ed.forward(25)
    else:
        ed.right(120)
        ed.forward(150)

wn.exitonclick()


