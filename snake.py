"""
Snake Class File.
Handles Snake object movements and methods.
"""
from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """
    This is the snake class, it handles all the logic for the snake within the game.
    """
    def __init__(self):
        """
        Initialisation function gives the snake
        """
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        Initial creation of snake body, makes three turtles, puts them in their starting positions and then
        makes it so that they have their penup and adds the objects to the segment list.
        """
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake(self):
        """
        Function moves each segment from the back to the position of the segment in front, it then moves
        the first segment in the snake forward.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)

    def right(self):
        """
        If not facing left, faces snake right.
        :return: Null.
        """
        if self.segments[0].heading() == 180:
            return
        else:
            self.segments[0].setheading(0)

    def up(self):
        """
        If not facing down, faces snake up.
        :return: Null.
        """
        if self.segments[0].heading() == 270:
            return
        else:
            self.segments[0].setheading(90)

    def left(self):
        """
        If not facing right, faces snake left.
        :return: Null.
        """
        if self.segments[0].heading() == 0:
            return
        else:
            self.segments[0].setheading(180)

    def down(self):
        """
        If not facing up, faces snake down.
        :return: Null.
        """
        if self.segments[0].heading() == 90:
            return
        else:
            self.segments[0].setheading(270)

