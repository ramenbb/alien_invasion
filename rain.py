import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
	"""A class to represent a single raindrop."""

	def __init__(self, ai_settings, screen):
		"""Initialize the raindrop and set its starting position."""
		super(Raindrop, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the rain image and set its rect attribute.
		self.image = pygame.image.load('images/rain.png')
		self.image = pygame.transform.scale(self.image,(50,50))
		self.rect = self.image.get_rect()

		# Start each new raindrop near the top left of the screen.
		#self.rect.x = self.rect.width
		#self.rect.y = self.rect.height

		# Store the raindrop's exact position.
		self.y = float(self.rect.y)

	def blitme(self):
		"""Draw the raindrop at its current location."""
		self.screen.blit(self.image, self.rect)	

	def check_bottom(self):
		""" Return True if rain is at bottom of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.bottom:
			return True

	def update(self):
		"""Move the rain down."""
		self.y += (self.ai_settings.raindrop_speed_factor)
		self.rect.y = self.y