import sys

import pygame

from rain import Raindrop

def update_screen(ai_settings, screen, rains):
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	rains.draw(screen)

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def get_number_rain_x(ai_settings, rain_width):
	"""Determine the number of raindrops that fit in a row."""
	available_space_x = ai_settings.screen_width - 2 * rain_width
	number_rain_x = int(available_space_x / (2 * rain_width))
	return number_rain_x

def get_number_rows(ai_settings, rain_height):
	"""Determine the number of rows of rain that fit on the screen."""
	available_space_y = (ai_settings.screen_height - (3 * rain_height) - 200)
	number_rows = int(available_space_y / (2 * rain_height))
	return number_rows

def create_rain(ai_settings, screen, rains, rain_number, row_number):
	"""Create rain and place it in the row."""
	rain = Raindrop(ai_settings, screen)
	rain_width = rain.rect.width
	rain.x = rain_width + 2 * rain_width * rain_number
	rain.rect.x = rain.x
	rain.rect.y = rain.rect.height + 2 * rain.rect.height * row_number
	rains.add(rain)

def create_cloud(ai_settings, screen, rains):
	"""Create a full fleet of rain."""
	# Create rain and find the number of raindrops in a row.
	# Spacing between each raindrop is equal to one raindrop width.
	rain = Raindrop(ai_settings, screen)
	number_rain_x = get_number_rain_x(ai_settings, rain.rect.width)
	number_rows = get_number_rows(ai_settings, rain.rect.height)

	# Create the cloud of raindrops.
	for row_number in range(number_rows):
		for rain_number in range(number_rain_x):
			create_rain(ai_settings, screen, rains, rain_number, row_number)

def check_row_bottom(ai_settings, rains):
	"""Respond appropriately if any raindrops have reached an edge."""
	for raindrop in rains.sprites():
		if raindrop.check_bottom():
			#rains.remove(raindrop)
			break

def update_rains(ai_settings, rains):
	"""
	Check if the row of raindrops is at the bottom,
	and then update the positions of all raindrops in the fleet
	"""
	check_row_bottom(ai_settings, rains)
	rains.update()
