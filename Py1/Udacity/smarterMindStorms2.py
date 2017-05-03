import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("cyan")
    brad = turtle.Turtle()
    feature(brad)
    for i in range(1,37):
        draw(brad, "square")
        brad.right(10)
    draw(brad, "circle")
    draw(brad, "triangle")
    window.exitonclick()
def feature(brad):
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
def draw(brad, shape):
    if shape == "square":
        for i in range(1,5):
            brad.forward(100)
            brad.right(90)
    elif shape == "circle":
        brad.shape("arrow")
        brad.color("blue")
        brad.circle(100)
    else:
        count = 0
        while(count < 3):
            brad.forward(100)
            brad.right(120)
            count = count + 1
draw_square()
