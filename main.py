"""
Snake game. V1.0
Written by Harry Perriton
"""

# Import classes from turtle module and time module.
from turtle import Screen
import time
from snake import Snake

# Calls a new screen object locally and a new "snake" object from the snake class.
screen = Screen()

# Screen setup variables, set screen resolution, background colour and title.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Creates the snake within the screen once you've made the screen.
snake = Snake()
time.sleep(2)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Removes animations but you have to call screen updates.
screen.tracer(0)

# While game is on, loop every 0.1 seconds, updating the screen.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()  # This moves the snake forward continuously.

screen.exitonclick()
