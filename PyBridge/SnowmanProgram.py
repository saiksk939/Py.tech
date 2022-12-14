from importlib.util import spec_from_file_location
import turtle 
s=turtle.Screen()
t=turtle.Turtle()
t.pensize(3)
t.speed(0)
turtle.screensize(canvheight=600, canvwidth=600, bg = 'orange' )
t.pencolor("black")
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

draw_circle("white", 30, 0, -40)
draw_circle("white", 40, 0, -100)
draw_circle("white", 60, 0, -200)

draw_circle("white", 2, -10, -10)
draw_circle("white", 2, 10, -10)
draw_circle("red", 3, 0, -15)

draw_circle("white", 2, 0, -35)
draw_circle("white", 2, 0, -45)
draw_circle("white", 2, 0, -55)

t.penup()
t.goto(-15, -35)
t.pendown()
t.pensize(5)
t.goto(-75, -50)

t.penup()
t.goto(15, -35)
t.pendown()
t.pensize(5)
t.goto(75, -50)

t.penup()
t.goto(-35, 8)
t.color("black")
t.pensize(6)
t.pendown()
t.goto(35, 8)

t.goto(30, 8)
t.fillcolor("skyblue")
t.begin_fill()
t.left(90)
t.forward(15)
t.left(90)
t.forward(60)
t.left(90)
t.forward(15)
t.end_fill()
t.hideturtle()
s.exitonclick()