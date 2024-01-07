"""
This file manages the scoreboard.
"""

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.setpos(0, 260)
        self.write(f"Score: {self.current_score}", False, "center", ('Arial', 18, 'normal'))

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", False, "center", ('Arial', 18, 'normal'))
