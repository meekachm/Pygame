import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height)) REMOVE!
    # self.surf.fill((255, 0, 255)) REMOVE!
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Make an instance of GameObject
# box = GameObject(120, 300, 50, 50) REMOVE!
apple = GameObject(120, 300, 'apple.png') # ADD!
strawberry = GameObject(240, 300, 'strawberry.png')
apple2 = GameObject(360, 300, 'apple.png')
strawberry2 = GameObject(120, 200, 'strawberry.png')
apple3 = GameObject(240, 200, 'apple.png')
strawberry3 = GameObject(360, 200, 'strawberry.png')
apple4 = GameObject(120, 100, 'apple.png')
strawberry4 = GameObject(240, 100, 'strawberry.png')
apple5 = apple5 = GameObject(360, 100, 'apple.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # box.render(screen) REMOVE!
    apple.render(screen) # ADD!
    strawberry.render(screen)
    apple2.render(screen)
    strawberry2.render(screen)
    apple3.render(screen)
    strawberry3.render(screen)
    apple4.render(screen)
    strawberry4.render(screen)
    apple5.render(screen)

    # Update the window
    pygame.display.flip()
