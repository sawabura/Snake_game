from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
import time
from borders import Borders

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
# anim off
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")




game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.snake_move()
	# Detect collision with food
	if snake.head.distance(food) < 15:
		scoreboard.increase_score()
		food.disappear_repeat()
		snake.get_bigger()
	# Detect collision with wall

	if snake.head.xcor() > 280 or\
		snake.head.xcor() < - 280 or\
		snake.head.ycor() > 280 or\
		snake.head.ycor() < -280:

		scoreboard.reset_score()
		snake.reset_snake()

	# Detect collision with tail
	for square in snake.list_of_squares[1:]:
		if snake.head.distance(square) < 10:
			scoreboard.reset_score()
			snake.reset_snake()






screen.exitonclick()
