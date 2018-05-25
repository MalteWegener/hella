from helpers import reflectray, reflectvel
import numpy as np
import pygame
import sys
import matplotlib.pyplot as plt

def nothing():
	return None

pos = (50,50)
vel = [43,0]
lines = [[(300,0),(140,220)],[(0,400),(500,400)],[(0,1),(0,500)],[(0,500),(500,500)],[(500,500),(500,1)],[(500,0),(0,0)]]

pygame.init()
screen = pygame.display.set_mode((500,500))

lastt=0

clock = pygame.time.Clock()

while True:
	currentt = pygame.time.get_ticks()

	dt = (currentt-lastt)/1000

	screen.fill((0,0,0))

	vel[1]+= 50*dt
	nextpos = (pos[0]+vel[0]*dt,pos[1]+vel[1]*dt)

	wasref = False
	for line in lines:
		tmp = reflectray(line[0],line[1],pos,nextpos)
		tvel = reflectvel(line[0],line[1],vel)
		if tmp is not None:
			pos = tmp
			vel = tvel
			wasref = True
			break
		else:
			continue



	if not wasref:
		pos = nextpos

	pos = (pos[0],pos[1])
	drawpos = (int(pos[0]),int(pos[1]))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	for lin in lines:
		pygame.draw.line(screen,(255,0,0), lin[0],lin[1])
	pygame.draw.circle(screen,(0,255,0),drawpos,5)
	lastt = currentt
	pygame.display.update()
	clock.tick(50)
