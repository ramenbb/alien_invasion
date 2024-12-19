import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from rain import Raindrop
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Steady rain")
	bg_color = (230, 230, 230)

	rains = Group()
	rain = Raindrop(ai_settings, screen)

	# Create the cloud.
	gf.create_cloud(ai_settings, screen, rains)


	# Start the main loop for the game.
	while True:

		gf.update_screen(ai_settings, screen, rain)
		gf.update_rains(ai_settings, rains)

run_game()
