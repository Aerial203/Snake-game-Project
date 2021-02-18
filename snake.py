from turtle import Turtle
SNAKE_BODY_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Creates the body of the snake"""
        self.snake_body_seg = []
        self.create_snake()
        self.head = self.snake_body_seg[0]

    def create_snake(self):
        for position in SNAKE_BODY_POSITION:
            self.add_snake_segment(position)

    def add_snake_segment(self, position):
        snake_seg = Turtle(shape="square")
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(position)
        self.snake_body_seg.append(snake_seg)

    def extend(self):
        self.add_snake_segment(self.snake_body_seg[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body_seg) - 1, 0, -1):
            new_x = self.snake_body_seg[seg_num - 1].xcor()
            new_y = self.snake_body_seg[seg_num - 1].ycor()
            self.snake_body_seg[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
