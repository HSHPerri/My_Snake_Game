"""
This file manages the scoreboard.
"""

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # This set of instructions is for the scoreboard at the top.
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.setpos(0, 260)
        self.write(f"Score: {self.current_score}", False, "center", ('Arial', 18, 'normal'))

        # This is the turtle for the hi score.
        self.hi_score = 0
        self.hi_score = Turtle()
        self.hi_score.color("yellow")
        self.hi_score.penup()
        self.hi_score.goto(30, 0)
        self.hi_score.hideturtle()

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", False, "center", ('Arial', 18, 'normal'))

    def hi_score_check_and_store(self):
        self.current_score = 0
        self.clear()
        self.write(f"Score: {self.current_score}", False, "center", ('Arial', 18, 'normal'))
