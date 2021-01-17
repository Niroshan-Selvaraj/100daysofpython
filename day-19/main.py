from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","green","yellow","blue","orange","purple"]
is_game_on = False

def place_all_turtle(turtle_count, start_x_position, start_y_position):
    for n in range(turtle_count):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(colors[n])
        new_turtle.goto(start_x_position, start_y_position)
        all_turtles.append(new_turtle)
        start_y_position += 50
    print(all_turtles)
    return all_turtles

turtles = place_all_turtle(6,-230,-130)

if user_bet:
    is_game_on = True
while is_game_on:
    for a_turtle in turtles:
        if a_turtle.xcor() > 230:
            is_game_on = False
            winning_color = a_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!" )
        rand_distance = random.randint(0,10)
        a_turtle.forward(rand_distance)













screen.exitonclick()
