# Import and initialize pygame
import pygame 
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Create the game loop
running = True 
while running: 
	# Looks at events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# # Clear the screen
	# screen.fill((255, 255, 255))
	# # Draw a circle
	# color = (255, 0, 255)
	# position = (250, 250)
	# pygame.draw.circle(screen, color, position, 75)
	# # Update the display
	# pygame.display.flip()

	
	# # Challenge 1
	# # Clear the screen
	# screen.fill((255, 255, 255))

	# # Your drawing here
	# colors = [(235, 61, 30), (96, 209, 96), (252, 140, 3), (99, 211, 255), (255, 213, 0)]
	# position = [(100, 100), (100, 400), (400, 100), (400, 400), (250, 250)]
	# sizes = [50, 50, 50, 50, 50]

	# for i in range(5):
	# 	pygame.draw.circle(screen, colors[i], position[i], sizes[i])

	# Challenge 2
	# Clear the screen
	screen.fill((255, 255, 255))

	# Your drawing here
	colors = [(89, 88, 88), (89, 88, 88), (89, 88, 88), (89, 88, 88), (89, 88, 88), (89, 88, 88), (89, 88, 88), (89, 88, 88), (89, 88, 88)]
	position = [(100, 100), (250, 100), (400, 100), (100, 250), (250, 250), (400, 250), (100, 400), (250, 400), (400, 400)]
	sizes = [50] * 9
	
	for i in range(9):
		if i < 3:
			pygame.draw.circle(screen, colors[i], position[i], sizes[i])
		elif 3 <= i < 6:
			pygame.draw.circle(screen, colors[i], position[i], sizes[i])
		else:
			pygame.draw.circle(screen, colors[i], position[i], sizes[i])


	# Update the display
	pygame.display.flip()