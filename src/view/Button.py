### -------------------------------------------- ###
import pygame
import time
### -------------------------------------------- ###

class Button(object):
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.blockedUntil = 0

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		currentTime = pygame.time.get_ticks()
		if currentTime < self.blockedUntil:
			return action

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
				self.blockedUntil = currentTime + 500

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action