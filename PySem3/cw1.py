import numpy as np
import time 
from visual import *


scene = display(width = 500, height = 500)
scene.range = 10

ball = sphere ( pos = np.random.uniform(-4, 4, 3), radius = 0.8, color= (0,0,0),make_trail =True )

wallR = box (pos=(5,0,0), size = (1,11,11), color = color.red)
wallL = box (pos=(-5,0,0), size = (1,11,11), color = color.blue)
wallU = box (pos=(0,5,0), size = (11,1,11), color = color.cyan)
wallD = box (pos=(0,-5,0), size = (11,1,11), color = color.green)
wallB = box (pos=(0,0,-5), size = (11,11,1), color = (1,1,1))

#kula w ruch
t=0
dt = 0.008
ball.vel=vector(np.random.uniform(-4, 4, 3))


time.sleep(1)
while 1:
	rate(1000)
	ball.pos = ball.pos + ball.vel*dt
	if abs(ball.pos.x) >= wallR.pos.x-1:
		ball.vel.x = -ball.vel.x
		ball.color=wallR.color
	if abs(ball.pos.x) >= wallL.pos.x-1:
		ball.vel.x = -ball.vel.x
		ball.color=wallL.color
	
	if abs(ball.pos.z) >= wallU.pos.y-1:
		ball.vel.z = -ball.vel.z
		ball.color=wallU.color
	if (ball.pos.z) >= wallD.pos.y+1:
		ball.vel.z = -ball.vel.z
		ball.color=wallD.color 

	if abs(ball.pos.y) >= wallD.pos.y-1:
		ball.vel.y = -ball.vel.y
		ball.color=wallB.color
	if abs(ball.pos.y) >= 4:
		ball.vel.y = -ball.vel.y
		ball.color = (0,0,0)

	
	t=t+dt

