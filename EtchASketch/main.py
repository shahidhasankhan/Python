import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def up():
    tim.setheading(90)
    tim.forward(20)


def down():
    tim.setheading(270)
    tim.forward(20)


def right():
    tim.setheading(0)
    tim.forward(20)


def left():
    tim.setheading(180)
    tim.forward(20)


screen.listen()

turtle.onkey(fun=up, key="w")
turtle.onkey(fun=down, key="s")
turtle.onkey(fun=left, key="a")
turtle.onkey(fun=right, key="d")


screen.exitonclick()
