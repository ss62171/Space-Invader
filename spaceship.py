import pygame
import time
import sys
from random import *
from pygame.locals import *

clock = pygame.time.Clock()	
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

w,h = 820,800
screen = pygame.display.set_mode((w,h))	

class Spaceship:
	def __init__(self,screen):
		self.x = 400
		self.y = 700
		self.screen = screen
		pygame.draw.rect(screen, white, [self.x,self.y,20,20])

	def pos(self):
		if(self.x >800):
			self.x = 800
		if(self.x < 0):
			self.x=0
		pygame.draw.rect(screen, white, [self.x,self.y,20,20])

