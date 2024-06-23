import turtle

from random_stuff import random_color


def draw_shape(sides):
    turtle.pencolor(random_color())
    for i in range(sides):
        turtle.right(360 / sides)
        turtle.forward(100)


turtle.colormode(255)
turtle.speed(0)

i = 1
while i > 0:
    draw_shape(i)
    i += 1
