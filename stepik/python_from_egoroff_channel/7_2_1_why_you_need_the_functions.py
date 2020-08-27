import turtle


def move(length, width):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)


def draw_rectangle(length, width):
    for i in range(2):
        move(length, width)


def draw_rectangle_color(length, width, color):
    turtle.color(color)
    turtle.begin_fill()
    draw_rectangle(length, width)
    turtle.end_fill()


def goto(x, y):
    turtle.color('black')
    turtle.goto(x, y)


turtle.speed(5)

draw_rectangle_color(200, 100, "green")
goto(250, 125)
draw_rectangle_color(120, 60, "red")
goto(390, 195)

input()
