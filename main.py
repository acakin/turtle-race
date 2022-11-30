from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
y_coord = [-75, -45, -15, 15, 45, 75]
turtles = []
for _ in range(0,6):
    t = Turtle(shape= "turtle")
    t.color(colors[_])
    t.penup()
    t.goto(x=-230, y=y_coord[_])
    turtles.append(t)
if user_bet:
    is_race_on = True
while is_race_on:
    for _ in turtles:
        if _.xcor() > 220:
            is_race_on = False
            winner = _.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")

            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        distance = random.randint(0, 10)
        _.forward(distance)
screen.exitonclick()
