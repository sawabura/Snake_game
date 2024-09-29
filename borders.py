from snake import Snake


class Borders(Snake):

	def __init__(self):
		super().__init__()
		border = [-290, 290]

	def border_kill(self):
		if self.head.ycor() > 290:
			answer = self.head.textinput(title="GAMEOVER",prompt="PLAY AGAIN y or n")
			if answer not in 'y':
				return screen.onclick()