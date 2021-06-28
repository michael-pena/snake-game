from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    move_distance = 20

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        start_length = 3
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for i in range(len(starting_positions)):
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(starting_positions[i])
            self.segments.append(snake_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(self.move_distance)

    def left(self):
        if self.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def up(self):
        if self.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def heading(self):
        return self.snake_head.heading()

    def grow(self):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(self.segments[-1].xcor() - 20, self.segments[-1].ycor())
        self.segments.append(snake_segment)