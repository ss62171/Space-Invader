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

class Shubham:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def draw(self,screen,colour):
		pygame.draw.circle(screen,colour,[self.x+5,self.y-20],10)

	def move(self,val):
		self.y -= val

class Bullet(Shubham):
	def __init__(self,x,y):
		Shubham.__init__(self,x,y)
		Shubham.draw(self,screen,blue)
		Shubham.move(self,2)
		

class Bullet2(Shubham):
	def __init__(self,x,y):
		Shubham.__init__(self,x,y)
		Shubham.draw(self,screen,green)
		Shubham.move(self,4)
