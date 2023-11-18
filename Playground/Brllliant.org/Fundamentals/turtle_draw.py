from turtle import *

color('red')
speed(0)
distance = 100
for j in range(120):
    for i in range(6):
        forward(distance)
        left(60)
        distance += 0.1
    left(3)


exitonclick()