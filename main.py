"""
Snake game - A Python take on Snake using Turtle
"""

# Import classes from turtle module and time module.
from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

# Calls a new screen object locally and a new "snake" object from the snake class.
screen = Screen()

# Screen setup variables, set screen resolution, background colour and title.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Creates the snake within the screen once you've made the screen.
snake = Snake()
food = Food()
scoreboard = Scoreboard()
time.sleep(1)

# Tells the screen to listen to key presses and what functions to call when it
# recognises them.
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
    time.sleep(0.08)

    snake.move_snake()  # This moves the snake forward continuously.

    if snake.snake_head.distance(food) < 15:
        food.move_food()
        scoreboard.update_score()
        snake.new_segment()

screen.exitonclick()
