import turtle
from math import sqrt,dist
n = 50

def multi_hex1(instance,pos=(0,0)):
    x1 , y1 = pos
    instance.teleport(x=x1,y=y1)

    for j in range(6):
        instance.right(120)
        for k in range(5):
            instance.forward(50)
            instance.right(60)
    for i in range(6):
        instance.forward(50)
        instance.left(60)

def multi_hex2(instance,pos=(0,0)):
    x1 , y1 = pos
    instance.teleport(x=x1,y=y1)

    for j in range(6):
        instance.left(120)
        for k in range(5):
            instance.forward(50)
            instance.left(60)
    for i in range(6):
        instance.forward(50)
        instance.right(60)


wn = turtle.Screen()
wn.bgcolor("black")

vicious = turtle.Turtle()
vicious.pensize(3)
vicious.color("grey","orange")
vicious.left(120)
vicious.speed(9)

multi_hex1(vicious)

spike = turtle.Turtle()
spike.pencolor("blue")
spike.pensize("3")
spike.speed(9)

spike.teleport(x=100,y=50*sqrt(3))
spike.left(60)
spike.penup()
spike.forward(50)
spike.pendown()
pos1 = spike.pos()

multi_hex1(spike,pos1)
multi_hex1(spike,(pos1[0]-300,pos1[1]))
spike.left(120)
multi_hex1(spike,(pos1[0]-300,-pos1[1]))
multi_hex1(spike,(pos1[0],-pos1[1]))

ed = turtle.Turtle()
ed.pencolor("orange")
ed.pensize(3)
ed.speed(9)

ed.teleport(pos1[0],-pos1[1])
ed.penup()
ed.forward(25)
ed.left(90)
ed.forward(25*sqrt(3))
ed.right(90)
ed.forward(100)
ed.left(60)
ed.forward(50)
ed.pendown()
pos2 = ed.pos()
a1 , b1 = pos2

multi_hex1(ed,pos2)

ed.left(120)
multi_hex2(ed,(pos2[0]-600,pos2[1]))

a2,b2 = ed.pos()

ed.left(60)
multi_hex2(ed,(a2-50,b2+150*sqrt(3)))
multi_hex2(ed,(a2-50,b2-100*sqrt(3)))

ed.left(60)
multi_hex1(ed,(a1,b1+150*sqrt(3)))
multi_hex1(ed,(a1,b1-100*sqrt(3)))

wn.exitonclick()
