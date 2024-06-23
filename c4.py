import turtle

from random_stuff import random_color, random_direction


def draw_line():
    turtle.pencolor(random_color())
    turtle.right(random_direction())
    turtle.forward(10)


turtle.colormode(255)
turtle.speed(0)
turtle.pensize(4)

while True:
    draw_line()
