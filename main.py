import turtle

import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
turtle.colormode(255)
tim.penup()
tim.goto(-225, -275)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

color_list = [(239, 230, 221), (0, 0, 0), (231, 153, 82), (119, 171, 203), (39, 110, 159), (240, 200, 80), (160, 59, 83), (200, 83, 111), (215, 132, 159), (23, 137, 102), (223, 83, 61), (119, 189, 154), (158, 164, 48), (188, 212, 222), (244, 156, 174), (47, 171, 134), (230, 197, 214), (28, 164, 194), (197, 221, 212), (161, 74, 52), (9, 102, 78), (242, 164, 153), (115, 43, 56), (108, 115, 171), (151, 214, 194), (148, 208, 225), (178, 181, 215), (42, 60, 103), (110, 46, 44), (34, 66, 83)]
for row in range(0, 10):
    tim.goto(-225, tim.ycor() + 50)
    for column in range(0, 10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)










screen = Screen()
screen.exitonclick()
