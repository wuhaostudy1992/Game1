import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		'''Initialize the ship and set its starting position'''
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Load the ship image and get its rect
		self.image  = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#start each new ship at bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		#Ship speed
		self.ship_move_unit = 1
		self.ship_speed_factor = 1.5
	
	def update(self):
		'''Update the ship's position based on the movement flag'''
		# Update the ship's value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ship_move_unit #self.rect.width
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ship_move_unit #self.rect.width
		#elif self.moving_up:
		#	self.rect.centery -= self.ship_move_unit #self.rect.height
		#elif self.moving_down:
		#	self.rect.centery += self.ship_move_unit #self.rect.height
		
		self.rect.centerx = self.center
		
	def blitme(self):
		'''Draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)
