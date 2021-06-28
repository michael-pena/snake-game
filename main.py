from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# create a file or read a file called high score and obtain the current high score in the file
# display this value in the screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True

# start moving forward
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food distance method
    if snake.snake_head.distance(food) < 15:
        print("food eaten.")
        food.move()
        snake.grow()
        scoreboard.increase_score()

    # detect collision with walls
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or\
            snake.snake_head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    # detect collision with tail
    for segment in range(1, len(snake.segments)):
        if snake.snake_head.distance(snake.segments[segment]) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
