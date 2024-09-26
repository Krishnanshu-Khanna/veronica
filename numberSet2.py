import turtle
from time import sleep

def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.addshape("body.gif")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    t.color("darkblue")
    turtle.title('Guess the Number')
    t.penup()
    t.goto(-200, 250)
    t.write("Guess it and remember it! Go to the Image", font=("Arial", 24, "bold"))
    t.hideturtle()
    return t, screen

def draw_border(t):
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    t.pensize(5)
    t.color("black")
    t.fillcolor("lightgray")
    t.begin_fill()
    for _ in range(4):
        t.forward(400)
        t.right(90)
    t.end_fill()

def draw_number_7(t):
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.pensize(10)
    t.color("red")
    t.forward(120)
    sleep(0.7)
    t.right(135)
    t.forward(170)
    sleep(0.7)
    t.right(135)
    t.forward(120)
    sleep(0.5)

def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def decorate_background(t):
    draw_star(t, -150, 150, 30)
    draw_star(t, 100, 180, 20)
    draw_star(t, 0, -150, 40)

def display_message_and_image(t, screen):
    t.penup()
    t.goto(-100, -50)
    t.color("blue")
    sleep(4)
    image_turtle = turtle.Turtle()
    image_turtle.shape("body.gif")
    image_turtle.penup()
    image_turtle.goto(0, 0)

def main():
    t, screen = setup_turtle()
    draw_border(t)
    draw_number_7(t)
    decorate_background(t)
    display_message_and_image(t, screen)
    t.hideturtle()
    sleep(5)
    turtle.done()

main()
