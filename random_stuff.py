import random


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_direction():
    return random.randint(1, 4) * 90
