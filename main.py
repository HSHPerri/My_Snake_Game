"""
Snake game. V1.0
Written by Harry Perriton
"""

# Import classes from turtle module and time module.
from turtle import Turtle, Screen
import time

# Call new turtle and screen objects from turtle class.
my_turtle = Turtle()
screen = Screen()

# Screen setup variables, set screen resolution, background colour and title.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Removes animations but you have to call screen updates.
screen.tracer(0)

# Initial variables, empty list of segment pieces and 3 starting positions.
segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Initial starting setup - create three turtles that are square shaped and stack them up
# behind one another.
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# While game is on, loop every 0.1 seconds, updating the screen.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # For each segment in the defined range, update coordinates
    # of last segment to be the same as that of the next.
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # Finally, update front segment to be one square forward.
    segments[0].forward(20)

screen.exitonclick()
