from turtle import Turtle, Screen
import random
directions = [ 0 , 90, 180 ,270]

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)

def draw_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

angle = 5
total_circles = int(360 / angle)
for _ in range(total_circles):
    tim.pencolor(draw_color())
    tim.circle(100)
    tim.left(5)

screen.exitonclick()



