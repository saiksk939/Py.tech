import turtle
from turtle import *
from random import randint
title('Random Colors Circle')
bgcolor('black')
pencolor('yellow')
speed(0)
pensize(1)
x=1
while x<400:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    colormode(255)
    pencolor(r,g,b) 
    forward(50+x)
    right(90.991)
    x+=1
done()
