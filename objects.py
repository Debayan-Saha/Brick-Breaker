import main
import config 
import declaring
from colorama import Fore, init , Back , Style
from numpy import random
from time import time
init()

class Object():
	
	def __init__(self, obj, xp, yp):
		self.pos_x = xp
		self.pos_y = yp
		self.length = len(obj)
		self.shape = obj
  
	def cur_posx(self):
		return self.pos_x

	def cur_posy(self):
		return self.pos_y
	
	def get_length(self):
		return self.length

	def update_x(self, val):
		self.pos_x += val
		if self.pos_x < 3:
			self.pos_x = 3
		elif self.pos_x > (config.columns-8):
			self.pos_x = config.columns-8

	def clear(self):
		for i in range(self.length):
			declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =" "
	
	def render(self):
		for i in range(self.length):
			declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.WHITE + Fore.WHITE+ self.shape[i])
	
class Paddle(Object):
	
	def __init__(self, obj, xp, yp):
		super().__init__(obj, xp, yp)    
		
class Ball(Object):
	
	def __init__(self, obj, xp, yp):
		super().__init__(obj, xp, yp)    
		self.speedx = 0
		self.speedy = 0

	def start(self):
		self.speedx = 0
		self.speedy = 1
		if self.pos_x == declaring.obj_paddle.pos_x:
			self.speedx = -2
		elif self.pos_x == declaring.obj_paddle.pos_x+1:
			self.speedx = -1
		elif self.pos_x == declaring.obj_paddle.pos_x+3:
			self.speedx = 1
		elif self.pos_x == declaring.obj_paddle.pos_x+4:
			self.speedx = 2
	def paddle_collision(self):
		if self.pos_y >= config.rows - 4 and self.pos_y <= config.rows - 3:
			if config.fallingflag == 1:
				brickfall()
			if self.pos_x >= declaring.obj_paddle.pos_x and self.pos_x <= declaring.obj_paddle.pos_x+4:
				self.speedy *= -1
			if self.pos_x == declaring.obj_paddle.pos_x:
				self.speedx += -2
			elif self.pos_x == declaring.obj_paddle.pos_x+1:
				self.speedx += -1
			elif self.pos_x == declaring.obj_paddle.pos_x+3:
				self.speedx += 1
			elif self.pos_x == declaring.obj_paddle.pos_x+4:
				self.speedx += 2

	def wall_collision(self):
		if self.pos_y > config.rows - 3:
			config.lives -= 1
			n1 = random.randint(4, config.columns-8)
			n = random.randint(5)
			declaring.obj_ball.pos_x = n + n1
			declaring.obj_ball.pos_y = config.rows - 5 
			declaring.obj_paddle.pos_x = n1
			declaring.obj_paddle.pos_y = config.rows - 3
			config.startflag = 0
			declaring.obj_ball.speedx = 0
			declaring.obj_ball.speedy = 0  
		if self.pos_y < 4:
			self.speedy *= -1
		if self.pos_x < 4 or self.pos_x + self.speedx > config.columns-3:
			self.speedx *= -1

	def render(self):
		self.wall_collision()
		self.paddle_collision()
		self.pos_x += self.speedx
		self.pos_y -= self.speedy
		for i in range(self.length):
			declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Fore.YELLOW + self.shape[i])

class Brick(Object):
	
	def __init__(self, obj, xp, yp, weight):
		super().__init__(obj, xp, yp)    
		self.weight = weight

	def val_weight(self):
		return self.weight

	def explosion(self):
		neigh = [[self.pos_x, self.pos_y-2], [self.pos_x, self.pos_y+2], [self.pos_x-4, self.pos_y-2], [self.pos_x-4, self.pos_y+2], [self.pos_x-4, self.pos_y], [self.pos_x+4, self.pos_y-2], [self.pos_x+4, self.pos_y+2], [self.pos_x+4, self.pos_y]]
		for j in range(len(declaring.brick_Shape)):
			for i in range(len(declaring.brick_Shape[j])):
				for k in range(8):
					if declaring.brick_Shape[j][i].pos_x == neigh[k][0] and declaring.brick_Shape[j][i].pos_y == neigh[k][1]:
						if declaring.brick_Shape[j][i].weight == 5:
							declaring.brick_Shape[j][i].weight = 0
							declaring.brick_Shape[j][i].explosion()
						else:
							if declaring.brick_Shape[j][i].weight < 4:
								config.score += declaring.brick_Shape[j][i].weight*5
								config.levelscore += declaring.brick_Shape[j][i].weight*5
							declaring.brick_Shape[j][i].weight = 0
								
	def collision(self):
		if self.weight != 0:
			if self.pos_x == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight == 5:
					self.weight = 0
					self.explosion()
				elif self.weight > 0 and self.weight < 4:
					config.score += 5
					config.levelscore += 5
					self.weight -= 1
				if declaring.obj_ball.speedx == 0:
					declaring.obj_ball.speedy *= -1
				else:
					declaring.obj_ball.speedx *= -1

			if self.pos_x+2 == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight == 5:
					self.explosion()
				elif self.weight > 0 and self.weight < 4:
					config.score += 5
					config.levelscore += 5
					self.weight -= 1
				if declaring.obj_ball.speedx == 0:
					declaring.obj_ball.speedy *= -1
				else:
					declaring.obj_ball.speedx *= -1

			
			if self.pos_x+1 == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight == 5:
					self.explosion()
				elif self.weight > 0 and self.weight < 4:
					config.score += 5
					config.levelscore += 5
					self.weight -= 1
				declaring.obj_ball.speedy *= -1

	def collision_fall(self):
		if self.weight != 0:
			if self.pos_y == config.rows - 4:
				config.lives = 0

	def render(self):
		for i in range(self.length):
			if self.weight == 0:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =" "
			if self.weight == 1:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.RED + Fore.RED + self.shape[i])
			if self.weight == 2:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.MAGENTA + Fore.MAGENTA + self.shape[i])
			if self.weight == 3:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.BLUE + Fore.BLUE + self.shape[i])
			if self.weight == 4:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.CYAN + Fore.CYAN + self.shape[i])
			if self.weight == 5:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.YELLOW + Fore.YELLOW + self.shape[i])

class Rainbow(Brick):
	"""docstring for Rainbow"""
	def __init__(self, obj, xp, yp, weight):
		super().__init__(obj, xp, yp, weight)  
		self.check = 0
		
	def collision(self):
		if self.weight != 0:
			if self.pos_x == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight > 0 and self.weight < 4:
					self.weight -= 1
					self.check = 1
				if declaring.obj_ball.speedx == 0:
					declaring.obj_ball.speedy *= -1
				else:
					declaring.obj_ball.speedx *= -1

			if self.pos_x+2 == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight > 0 and self.weight < 4:
					self.weight -= 1
					self.check = 1
				if declaring.obj_ball.speedx == 0:
					declaring.obj_ball.speedy *= -1
				else:
					declaring.obj_ball.speedx *= -1

			
			if self.pos_x+1 == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight > 0 and self.weight < 4:
					self.weight -= 1
					self.check = 1
				declaring.obj_ball.speedy *= -1


	def render(self):
		if self.check == 0:
			self.weight = random.randint(1,4)
		for i in range(self.length):
			if self.weight == 0:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =" "
			if self.weight == 1:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.RED + Fore.RED + self.shape[i])
			if self.weight == 2:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.MAGENTA + Fore.MAGENTA + self.shape[i])
			if self.weight == 3:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.BLUE + Fore.BLUE + self.shape[i])

def levelskip():
	for j in range(len(declaring.brick_Shape)):
		for i in range(len(declaring.brick_Shape[j])):
			declaring.brick_Shape[j][i].clear()
	if(config.level ==2):
		declaring.obj_paddle.clear()
		declaring.obj_ball.clear()
		declaring.brick_Shape = declaring.shape(config.level)
		config.levelscore = 0
		n = random.randint(5)
		declaring.obj_ball.pos_x = n + 30
		declaring.obj_ball.pos_y = config.rows - 5 
		declaring.obj_paddle.pos_x = 30
		declaring.obj_paddle.pos_y = config.rows - 3
		config.startflag = 0
		declaring.obj_ball.speedx = 0
		declaring.obj_ball.speedy = 0
	elif(config.level >2):
		declaring.brick_Shape = declaring.shape(config.level)
		config.levelscore = 0
	else:
		declaring.obj_paddle.clear()
		declaring.obj_ball.clear()
		declaring.brick_Shape = declaring.shape(config.level)
		config.levelscore = 0
		n1 = random.randint(4, config.columns-8)
		n = random.randint(5)
		declaring.obj_ball.pos_x = n + n1
		declaring.obj_ball.pos_y = config.rows - 5 
		declaring.obj_paddle.pos_x = n1
		declaring.obj_paddle.pos_y = config.rows - 3
		config.startflag = 0
		declaring.obj_ball.speedx = 0
		declaring.obj_ball.speedy = 0

def brickfall():
	for j in range(len(declaring.brick_Shape)):
		for i in range(len(declaring.brick_Shape[j])):
			declaring.brick_Shape[j][i].clear()
	for j in range(len(declaring.brick_Shape)):
		for i in range(len(declaring.brick_Shape[j])):
			declaring.brick_Shape[j][i].pos_y += 1

class Boss(Brick):
	
	def __init__(self, obj, xp, yp, weight):
		super().__init__(obj, xp, yp, weight)

	def render(self):
		for i in range(self.length):
			if self.weight == 0:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =" "
			if self.weight == 1:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.RED + Fore.RED + self.shape[i])
			if self.weight == 4:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Back.CYAN + Fore.CYAN + self.shape[i])
			if self.weight == 6:
				declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Fore.WHITE+ self.shape[i])
	
	def collision(self):
		if self.weight != 0:
			if self.pos_x == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight == 6:
					config.health -= 1
					config.levelscore += 1					
				elif self.weight > 0 and self.weight < 4:
					config.score += 5
					self.weight -= 1
				if declaring.obj_ball.speedx == 0:
					declaring.obj_ball.speedy *= -1
				else:
					declaring.obj_ball.speedx *= -1

			if self.pos_x+2 == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight > 0 and self.weight < 4:
					config.score += 5
					self.weight -= 1
				if declaring.obj_ball.speedx == 0:
					declaring.obj_ball.speedy *= -1
				else:
					declaring.obj_ball.speedx *= -1

			
			if self.pos_x+1 == declaring.obj_ball.pos_x and self.pos_y == declaring.obj_ball.pos_y:
				if self.weight > 0 and self.weight < 4:
					config.score += 5
					self.weight -= 1
				declaring.obj_ball.speedy *= -1

class Bomb(Object):
	def __init__(self, obj, xp, yp):
		super().__init__(obj, xp, yp)
		self.speedy = 0
		self.flag = 0

	def render(self):
		check = time()
		if (int)(check) % 5 == 0:
			self.pos_y = declaring.brick_Shape[0][2].pos_y
			self.speedy = 1
			self.shape = config.bomb
			self.flag = 0
		if (self.flag == 0):
			self.pos_y += self.speedy
		self.collision_with_paddle()
		for i in range(self.length):
			declaring.obj_board.matrix[self.pos_y][i+self.pos_x] =(Fore.RED+ self.shape[i])

	def updateval(self, x):
		self.pos_x = x

	def collision_with_paddle(self):
		if self.pos_y >= config.rows - 4 and self.pos_y <= config.rows - 3:
			if self.pos_x >= declaring.obj_paddle.pos_x and self.pos_x <= declaring.obj_paddle.pos_x:
				self.flag = 1
				self.pos_y = 1
				config.lives -= 1
			elif self.pos_x >= declaring.obj_paddle.pos_x and self.pos_x <= declaring.obj_paddle.pos_x+1:
				self.flag = 1
				self.pos_y = 1
				config.lives -= 1
			elif self.pos_x >= declaring.obj_paddle.pos_x and self.pos_x <= declaring.obj_paddle.pos_x+2:
				self.flag = 1
				self.pos_y = 1
				config.lives -= 1
			elif self.pos_x >= declaring.obj_paddle.pos_x and self.pos_x <= declaring.obj_paddle.pos_x + 3:
				self.flag = 1
				self.pos_y = 1
				config.lives -= 1
			elif self.pos_x >= declaring.obj_paddle.pos_x and self.pos_x <= declaring.obj_paddle.pos_x + 4:
				self.flag = 1
				self.pos_y = 1
				config.lives -= 1
				

		if self.pos_y > config.rows -3:
			self.speedy = 0
			self.flag = 1
			self.pos_y = 1
			self.shape = [' ']