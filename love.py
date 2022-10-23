from turtle import *
import random

ran = [
    "red",
    "green",
    "blue",
    "purple",
    "yellow",
    "sky blue",
    "hot pink",
    "orange",
    "black",
    "indigo",
    "violet",
    "navy blue",
    
  
    "grey",
]
while True:
    for i in ran:
        speed(14)
        color(i)
        begin_fill()
        pensize(3)
        left(50)
        forward(133)
        circle(50, 200)
        right(140)
        circle(50, 200)
        forward(133)
        end_fill()
