from colorama import init, Style
import numpy as np 
import config 
from time import time
init()
class Board():
	
	height = int(config.rows)
	length = int(config.columns)

	def __init__(self):
		self.matrix = [[ " " for i in range(self.length)] for j in range(self.height)]
		self.boundary()

	def render(self):
		if config.level >=2:
			print("LIVES LEFT: ", int(config.lives), "   SCORE: ", int(config.score), "   TIME: ", int(config.time), "   LEVELS: ", 3,"HEALTH: ", int(config.health))
		else:
			print("LIVES LEFT: ", int(config.lives), "   SCORE: ", int(config.score), "   TIME: ", int(config.time), "   LEVELS: ", int(config.level+1))
		for j in range(self.height):
			bo = []
			for i in range(self.length):
				bo.append(self.matrix[j][i] + Style.RESET_ALL)
			s=''
			print(s.join(bo))


	def boundary(self):
		for i in range(3, self.length-3):
			self.matrix[2][i] = "="
			self.matrix[self.height-1][i] = "="
		