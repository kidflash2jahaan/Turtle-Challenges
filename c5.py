import turtle

from random_stuff import random_color


def draw_circle(frequency):
    turtle.pencolor(random_color())
    turtle.right(frequency)
    turtle.circle(100)


turtle.colormode(255)
turtle.speed(0)

frequency = 5

for i in range(int(360 / frequency)):
    draw_circle(frequency)

turtle.mainloop()
