from turtle import *

def ellipse(rad):
    for _ in range(2):
        circle(rad,90)
        circle(rad//2,90)

def eye(rad, high=0):
    up()
    setx(xcor() + rad)
    down()
    circle(rad,180)
    fd(high)
    circle(rad,180)
    fd(high)

def square(lado):
    for _ in range(4):
        fd(lado)
        lt(90)