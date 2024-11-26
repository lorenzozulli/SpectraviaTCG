### -------------------------------------------- ###
import pygame
import time
### -------------------------------------------- ###

class Button(object):
	def __init__(self, x, y, image, text, text_color, font, font_size, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.text = text
		self.text_color = text_color
		self.font = font
		self.font_size = font_size
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
		
		text_surface = self.font.render(self.text, True, self.text_color)
		surface.blit(text_surface, (self.rect.x + 50, self.rect.y + 40))

		return action