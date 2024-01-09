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


def snake_game_begin():
    # If the snake isn't at it's beginning position, call the reset function.
    if snake.snake_head.position() != (0, 0) or len(snake.segments) > 3:
        scoreboard.hi_score_check_and_store()
        snake.clear_game_over_message()
        snake.game_reset()

    # While game is on, loop every 0.08 seconds (12.5 frames per second), updating the screen with each frame.
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.08)

        snake.move_snake()  # This moves the snake forward continuously.

        # If snake head collides with a food spot, update its position and player score.
        if snake.snake_head.distance(food) < 15:
            food.move_food()
            scoreboard.update_score()
            snake.new_segment()

        # If snake collides with a wall, stop the snake moving and give game over message.
        # Had to separate out into two if statements otherwise it only recognises two walls as death pointers.
        # First group checks the X coordinate.
        if snake.check_wall_collision():
            game_is_on = False
            snake.game_over_message()

        # If snake collides wih a segment in its tail, the game is over.
        elif snake.check_tail_collision() is True:
            game_is_on = False
            snake.game_over_message()


screen.onkey(snake_game_begin, "space")

screen.exitonclick()
