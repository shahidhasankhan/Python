import turtle
import random

turtle.colormode(255)

SHAPES = [4, 5, 6, 7, 8, 9, 10]
COLORS = ["red", "green", "blue", "purple", "orange", "gold"]
DIRECTIONS = [90, 180, 270, 360]


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_color = (r,g,b)
    return my_color


timmy = turtle.Turtle()
timmy.shape("turtle")

# for shape in SHAPES:
#     timmy.color(random.choice(COLORS))
#     for sides in range(shape):
#         timmy.forward(100)
#         timmy.right(360/shape)

timmy.speed(10)
timmy.pensize(5)

# for _ in range(100):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(DIRECTIONS))

for angle in range(0,360,20):
    timmy.setheading(angle)
    timmy.color(random_color())
    timmy.circle(100)

my_screen = turtle.Screen()
my_screen.exitonclick()
