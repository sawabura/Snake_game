
from turtle import Turtle, colormode
from random import randint


class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape('circle')
		colormode(255)
		self.penup()
		self.color((randint(1, 255), randint(1, 255), randint(1, 255)))
		self.shapesize(0.5, 0.5)
		self.speed('fastest')
		self.disappear_repeat()

	def disappear_repeat(self):
		self.hideturtle()
		self.goto(x=randint(-280, 280), y=randint(-280, 280))
		self.showturtle()


