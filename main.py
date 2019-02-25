import pygame
import time
import sys
from random import *
from pygame.locals import *
import aliens
import bullets
import spaceship

clock = pygame.time.Clock()	
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)


#GAME RUNNING MODE
pygame.init()
w,h = 820,800
screen = pygame.display.set_mode((w,h))	
				
def run():
	clock = pygame.time.Clock()	
	gameExit = False
	ship = spaceship.Spaceship(screen)
	score = 0
	x,y,tim=300,0,0
	alien = [aliens.Alien(x,y,tim,red),]

	bullet = []
	bullet2 = []
	j=0
	count = 1
	counter = 1
	value = 10000
	level = 1
	

	while not gameExit:

		screen.fill((0,0,0))
		clock.tick(60)
		val = pygame.time.get_ticks()
		if(score > 3*level and value > 4001):
			value -= 2000
			level += 1


		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == pygame.K_a:
					ship.x -= 100
					pygame.draw.rect(screen, white, [ship.x,ship.y,20,20])

				if event.key == pygame.K_d:
					ship.x += 100
					pygame.draw.rect(screen, white, [ship.x,ship.y,20,20])

				if event.key == pygame.K_q:
					gameExit = True

				if event.key == pygame.K_SPACE:
					bullet.append(bullets.Bullet(ship.x,ship.y))

				if event.key == pygame.K_s:
					bullet2.append(bullets.Bullet2(ship.x,ship.y))
					
		ship.pos()	

		for i in alien:
			i.move(screen)

		for i in bullet:
			i.move(2)
			i.draw(screen,blue)

		for i in bullet2:
			i.move(4)
			i.draw(screen,green)
						
		for i in alien:
			if(val > i.tim+8000):
				alien.remove(i)

		for i in alien:
			for j in bullet:
				if i.x == j.x and i.y ==j.y:
					alien.remove(i)
					score += 1
					print (score)

					bullet.remove(j)

		for i in alien:
			for j in bullet2:
				if i.x == j.x and i.y==j.y:
					i.tim += 5000
					i.color = white
					bullet2.remove(j)

					
		if(val>(counter*value)):
			counter+=1
			x = randint(1, 8)
			y = randint(0, 1) 
			x*=100
			y*=100
			alien.append(aliens.Alien(x,y,val,red))	
				
								
		pygame.display.update()
run()
