"""
Snake Class File.
Handles Snake object movements and methods.
"""
from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        """
        Initialisation function gives the snake
        """
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

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
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].setheading(new_heading)

        self.segments[0].forward(20)

    def right(self):
        """
        If not facing left, faces snake right.
        :return: Null.
        """
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def up(self):
        """
        If not facing down, faces snake up.
        :return: Null.
        """
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def left(self):
        """
        If not facing right, faces snake left.
        :return: Null.
        """
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def down(self):
        """
        If not facing up, faces snake down.
        :return: Null.
        """
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def new_segment(self):
        """
        Function takes the position of the last segment in the chain and uses its heading to
        decide where to spawn a new one as it's moving around.
        :return:
        """
        # Last seg position is acquired from the last segment in chain.
        last_seg_position = self.segments[len(self.segments)-1].position()
        # print(last_seg_position)

        # assigning the x and y coordinates of the position to variables.
        last_seg_position_x = last_seg_position[0]
        last_seg_position_y = last_seg_position[1]

        # based on heading, create new segment 20 pixels away.
        # Follows same creation structure as initializing function.
        match self.segments[len(self.segments)-1].heading():
            # Case that heading is right.
            case 0:
                new_seg_position = last_seg_position_x - 20, last_seg_position_y
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(new_seg_position)
                self.segments.append(new_segment)

            # Case that heading is up.
            case 90:
                new_seg_position = last_seg_position_x, last_seg_position_y - 20
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(new_seg_position)
                self.segments.append(new_segment)

            # Case that heading is left.
            case 180:
                new_seg_position = last_seg_position_x + 20, last_seg_position_y
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(new_seg_position)
                self.segments.append(new_segment)

            # Case that heading is down.
            case 270:
                new_seg_position = last_seg_position_x, last_seg_position_y + 20
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(new_seg_position)
                self.segments.append(new_segment)

    def check_wall_collision(self):
        """
        Function serves to check whether snake head is beyond/at the limits of the wall. If
        yes, then it returns true, otherwise returns false. 
        """
        if self.segments[0].position()[0] >= 300  or self.segments[0].position()[0] <= -300:
            return True
        
        elif self.segments[0].position()[1] >= 300 or self.segments[0].position()[1] <= -300:
            return True

        else:
            return False