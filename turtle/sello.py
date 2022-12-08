from turtle import *
from client.figures import *

# Pen
pen(speed=10, pensize=4)
ht()


# Main circle
up()
r1 = 99
down()
circle(r1)


# Mouth
up()
r2 = 2*r1/3
setpos(-r2, r1)
right(90)
down()
circle(r2, extent=180)

# Lengua
# ellipse(20)


# Left eye
up()
high = 35
x = -r1/6
y = r1 + r1/2
setpos(x, y)
down()
eye(8, high)

# Right eye
up()
x = r1/6
setpos(x, y)
down()
eye(8, high)

# Cachetes
angle = 5

square(90)


# Loop
done()