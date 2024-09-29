from turtle import Turtle


class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		with open("data.txt", 'r+') as file:
			self.highscore = int(file.read())
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0, 260)
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score:{self.score} High Score: {self.highscore}", False, align="center", font=('Arial', 24, 'normal'))

	def increase_score(self):
		self.score += 1
		self.update_score()

	def reset_score(self):
		if self.score > self.highscore:
			self.highscore = self.score
			with open("data.txt", 'a+') as file:
				file.write(f"{self.highscore}")

		self.score = 0
		self.update_score()


	# def gameover(self):
	# 	self.goto(0, 0)
	# 	self.write(f"Your Score is :{self.score} , ITS GAMEOVER", False, align="center", font=('Arial', 24, 'normal'))
