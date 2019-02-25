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

class Alien:
	def __init__(self,x,y,tim,color):
		self.x = x
		self.y = y
		self.tim = tim
		self.color = color
	

	def move(self,screen):
			pygame.draw.rect(screen, self.color, [self.x,self.y,10,10])
