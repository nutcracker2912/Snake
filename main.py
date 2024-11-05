from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
score_board = ScoreBoard()

snake.create_snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True

while game_is_on:
    screen.update()
    sleep_time = 0.15
    time.sleep(sleep_time)
    snake.move()

    # Detect collision with wall.
    if (300 < snake.segments[0].xcor() or snake.segments[0].xcor() < -310 or
            310 < snake.segments[0].ycor() or snake.segments[0].ycor() < -310):
        score_board.game_over()
        game_is_on = False

    # Dectect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.food_relocator()
        score_board.add_one_to_score()
        snake.extend()

    # Detect collision with tail.
    for tail in range(1, len(snake.segments) - 1):
        if snake.segments[0].distance(snake.segments[tail]) < 15:
            score_board.game_over()
            game_is_on = False

screen.exitonclick()
