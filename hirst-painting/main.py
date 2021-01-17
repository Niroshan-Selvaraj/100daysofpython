import random
import turtle
# color_objects = colorgram.extract("61RQCX9SJKL.jpg",10)
# colors = []
# for color in color_objects:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors.append(new_color)
#
# print(colors)
color_list = [ (236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40), (184, 158, 46)]

tim = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
print(tim.position())
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
position = tim.position()
height = position[1]
width = position[0]

for _ in range(10):
    tim.setposition(width, height)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    height += 50.00

screen.exitonclick()