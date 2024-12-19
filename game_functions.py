import sys

import pygame

from bullet import Bullet
from rain import Raindrop

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right.
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# Move the ship to the left;
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):	
	"""Fire a bullet if limit not reached"""
	# Create a new bullet and add it to the bullets group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right.
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		# Move the ship to the left;
		ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
	# Watch for keyboard and mouse events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, rains, bullets):
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	rains.draw(screen)
	# Redraw all bullets behind ship and rain.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions
	bullets.update()

	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def get_number_rain_x(ai_settings, rain_width):
	"""Determine the number of raindrops that fit in a row."""
	available_space_x = ai_settings.screen_width - 2 * rain_width
	number_rain_x = int(available_space_x / (2 * rain_width))
	return number_rain_x

def get_number_rows(ai_settings, ship_height, rain_height):
	"""Determine the number of rows of rain that fit on the screen."""
	available_space_y = (ai_settings.screen_height - (3 * rain_height) - rain_height)
	number_rows = int(available_space_y / (2 * rain_height))
	return number_rows

def create_rain(ai_settings, screen, rains, rain_number, row_number):
	"""Create rain and place it in the row."""
	rain = Raindrop(ai_settings, screen)
	rain_width = rain.rect.width
	rain.x = rain_width + 2 * rain_width * rain_number
	rain.rect.x = rain.x
	rain.rect.y = rain.rect.height + 2 * rain.rect.height * row_number
	print(rain.rect.y)
	rains.add(rain)

def create_cloud(ai_settings, screen, ship, rains):
	"""Create a full fleet of rain."""
	# Create rain and find the number of raindrops in a row.
	# Spacing between each raindrop is equal to one raindrop width.
	rain = Raindrop(ai_settings, screen)
	number_rain_x = get_number_rain_x(ai_settings, rain.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, rain.rect.height)

	# Create the first row of raindrops.
	for row_number in range(number_rows):
		for rain_number in range(number_rain_x):
			create_rain(ai_settings, screen, rains, rain_number, row_number)

def check_row_bottom(ai_settings, rains):
	"""Respond appropriately if any raindrops have reached an edge."""
	for raindrop in rains.sprites():
		if raindrop.check_bottom():
			break

def update_rains(ai_settings, rains):
	"""
	Check if the row of raindrops is at the bottom,
	and then update the positions of all raindrops in the fleet
	"""
	check_row_bottom(ai_settings, rains)
	rains.update()
