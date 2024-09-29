import turtle
from turtle import Turtle
# CONSTANCE
DISTANCE = 20


class Snake:

	def __init__(self):
		self.goto_x = 0
		self.list_of_squares = []
		self.list_creation()
		self.head = self.list_of_squares[0]


	def reset_snake(self):
		for square in self.list_of_squares:
			square.goto(1000, 1000)
		self.list_of_squares.clear()
		self.list_creation()
		self.head = self.list_of_squares[0] # important!!! dont forget to add this , we doing everything in init becouse we want to initialize again

	def list_creation(self):
		for i in range(3):
			self.add_segment(i)

	def snake_move(self):

		for square_n in range(len(self.list_of_squares) - 1, 0, -1):
			self.list_of_squares[square_n].goto(
				self.list_of_squares[square_n - 1].xcor(), self.list_of_squares[square_n - 1].ycor()
			)

		self.list_of_squares[0].forward(DISTANCE)

	def add_segment(self, i):
		self.list_of_squares.append(Turtle(shape='square'))
		self.list_of_squares[i].color('white')
		self.list_of_squares[i].penup()
		self.list_of_squares[i].goto(x=self.goto_x, y=0)
		self.goto_x -= 20

	def add_segment_more_than_4(self, i):
		self.list_of_squares.append(Turtle(shape='square'))
		self.list_of_squares[i].color('white')
		self.list_of_squares[i].penup()
		self.list_of_squares[i].goto(x=self.list_of_squares[i - 1].xcor(), y=self.list_of_squares[i - 1].ycor())


	def get_bigger(self):
		# use
		self.add_segment_more_than_4(len(self.list_of_squares))

	def up(self):
		if self.head.heading() != 270:
			self.head.setheading(90)

	def down(self):
		if self.head.heading() != 90:
			self.head.setheading(270)

	def left(self):
		if self.head.heading() != 0:
			self.head.setheading(180)

	def right(self):
		if self.head.heading() != 180:
			self.head.setheading(0)
