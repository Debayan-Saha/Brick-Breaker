from board import *
from config import *
from objects import *
from numpy import random
from time import time 
n1 = random.randint(4, columns-8)
n = random.randint(5)

# initial_time = time()
obj_board = Board()
obj_ball = Ball(config.ball, n1+n, rows-5)
obj_paddle = Paddle(config.paddle, n1, rows-3)
obj_brick = Brick(config.brick, 11, 8, 3)
obj_bomb = Bomb(config.bomb, 11, 7)

brick_Shape = [[], [], [], [], []]

def unbr(val):
	if val >= 4:
		return 0
	else:
		return val

for i in range(11, 81, 4):
	r1 = 5
	r2 = random.randint(1,5)
	r3 = random.randint(1,5)
	r4 = random.randint(1,5)	
	if i >= 31 and i <= 65:
		brick_Shape[0].append(Brick(brick, i, 10, r2))
		brick_Shape[1].append(Brick(brick, i, 12, r1))
		brick_Shape[2].append(Brick(brick, i, 14, r3))
		brick_Shape[3].append(Brick(brick, i, 8, r3))
		brick_Shape[4].append(Rainbow(brick, i, 6, 1))
		config.psum += unbr(r2) + unbr(r3) + unbr(r4) 
	config.psum *= 5

def shape(level):
	if(level==1):
		config.psum = 0
		brick_Shape = [[], [], [], [], []]
		for i in range(11, 81, 4):
			r1 = 5
			r2 = random.randint(1,5)
			r3 = random.randint(1,5)
			r4 = random.randint(1,5)	
			if i <= 31 or i >= 57:
			# brick_Shape[0].appe	nd(Brick(brick, i, 8, r4))
				brick_Shape[0].append(Brick(brick, i, 10, r2))
				brick_Shape[1].append(Brick(brick, i, 12, r1))
				brick_Shape[2].append(Brick(brick, i, 14, r3))
				brick_Shape[3].append(Brick(brick, i, 8, r4))
				brick_Shape[4].append(Rainbow(brick, i, 6, 1))
				config.psum += unbr(r2) + unbr(r3) + unbr(r4)
		config.psum *= 5
		return brick_Shape
	
	elif (level==2):
		config.psum = 0
		brick_Shape = [[], [], []] 
		r2 = 6
		brick_Shape[0].append(Boss(config.dia_l, 30, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 31, 7, r2))
		brick_Shape[0].append(Boss(config.hor, 32, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 33, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 34, 7, r2))
		for i in range(5):
			brick_Shape[1].append(Boss(config.vert, 30+i, 8, r2))
		for i in range(0,20,6):
			brick_Shape[2].append(Boss(brick, 28+i, 11, 4))
		config.psum = 4
		obj_bomb.updateval(brick_Shape[0][2].pos_x)
		return brick_Shape

	elif(level==3):
		config.psum = 0
		brick_Shape = [[], [], [], []] 
		r2 = 6
		brick_Shape[0].append(Boss(config.dia_l, 30, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 31, 7, r2))
		brick_Shape[0].append(Boss(config.hor, 32, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 33, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 34, 7, r2))
		for i in range(5):
			brick_Shape[1].append(Boss(config.vert, 30+i, 8, r2))
		for i in range(0,30,6):
			brick_Shape[2].append(Boss(brick, 20+i, 11, 4))
		for i in range(15,75,4):
			brick_Shape[3].append(Boss(brick, i, 13, 1))
		config.psum = 3
		return brick_Shape

	elif(level==4):
		config.psum = 0
		brick_Shape = [[], [], [], []] 
		r2 = 6
		brick_Shape[0].append(Boss(config.dia_l, 30, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 31, 7, r2))
		brick_Shape[0].append(Boss(config.hor, 32, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 33, 7, r2))
		brick_Shape[0].append(Boss(config.dia_l, 34, 7, r2))
		for i in range(5):
			brick_Shape[1].append(Boss(config.vert, 30+i, 8, r2))
		for i in range(0,30,6):
			brick_Shape[2].append(Boss(brick, 20+i, 11, 4))
		for i in range(15,75,4):
			brick_Shape[3].append(Boss(brick, i, 12, 1))
		config.psum = 3
		return brick_Shape



def render_bricks():
	for j in range(len(brick_Shape)):
		for i in range(len(brick_Shape[j])):
			brick_Shape[j][i].render()
			brick_Shape[j][i].collision()
			brick_Shape[j][i].collision_fall()
		if config.level >=2:
			obj_bomb.clear()
			if obj_bomb.pos_y >= 7 and obj_bomb.pos_y <= 9:
				obj_bomb.updateval(brick_Shape[0][2].pos_x)
			obj_bomb.render()



def update(x):
	for j in range(2):
		for i in range(len(brick_Shape[j])):
			brick_Shape[j][i].clear()
			# obj_bomb.update_x(x)
			brick_Shape[j][i].pos_x = int(x) + i
			if brick_Shape[j][i].pos_x < 3 + i:
				brick_Shape[j][i].pos_x = 3 + i
			elif brick_Shape[j][i].pos_x > (config.columns-8+i):
				brick_Shape[j][i].pos_x = config.columns-8+i
	obj_bomb.clear() 
	if obj_bomb.pos_y >= 7 and obj_bomb.pos_y <= 9:
		obj_bomb.updateval(brick_Shape[0][2].pos_x)

