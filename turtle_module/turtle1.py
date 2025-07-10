import turtle

win = turtle.Screen()

big_dawg = turtle.Turtle()
big_dawg.color("blue","green")
big_dawg.begin_fill()

big_dawg.forward(100)
big_dawg.left(90)
big_dawg.forward(50)
big_dawg.left(90)
big_dawg.forward(100)
big_dawg.left(90)
big_dawg.forward(50)

big_dawg.end_fill()

win.exitonclick()
