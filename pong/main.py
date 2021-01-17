from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

#Create the Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#Create Paddles that responds to Key Presses
screen.listen()

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = Ball()

#ball.move()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
