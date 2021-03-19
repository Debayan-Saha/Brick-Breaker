from input import *
import os
from declaring import *
import config
from time import time, sleep
if __name__ == "__main__":
	obj = Get()
	while(1):
		if config.timeflag == 0:
			initial_time = time()
			config.timeflag =1
		obj_paddle.clear()
		obj_ball.clear()	
		# obj_brick.clear()
		val = input_to(obj)
		sys.stdout.write("\033c")
		config.time = time() - initial_time
		if val != None:
			sleep(0.05)
		if val == 'q' or val =='Q' :
			print("Game over, You Quit the game")
			break
		elif int(config.lives) == 0:
			print("Game over, You were not able to complete the game")
			break
		elif int(config.level) > 4:
			print("Game over")
			break

		else:
			if val == 's' or val == 'S':
				if int(config.startflag) == 0:
					obj_ball.start()
					config.startflag = 1	
			elif val == 'a' or val =='A':
				if int(config.startflag) == 0:
					obj_ball.update_x(-1)
				obj_paddle.update_x(-1)
				if config.level >= 2:
					valx=obj_paddle.cur_posx()
					update(valx)
			elif val == 'd' or val =='D':
				if int(config.startflag) == 0:
					obj_ball.update_x(1)
				obj_paddle.update_x(1)
				if config.level >= 2:
					valx=obj_paddle.cur_posx()
					update(valx)
			elif val == 'x' or val =='X':
				config.fallingflag=0
				config.level +=1
				if int(config.level) > 2:
					print("Game over")
					break 
				if int(config.level) <= 2:
					levelskip()
				config.leveltime = time()
		
		if int(time()-config.leveltime)>20:
			if int(config.level) <= 1:
				config.fallingflag = 1  
		render_bricks()
		# render_explo()
		if config.levelscore == config.psum:
			config.fallingflag=0
			config.level +=1
			if int(config.level) > 4:
				print("Congratulations!!!")
				break
			config.leveltime = time()
			levelskip()
		# obj_brick.render()
		obj_ball.render()
		obj_paddle.render()
		obj_board.render()
		
	print("Total score = ", config.score, "Total Time Spent = ", int(config.time))
	# print(config.psum)
