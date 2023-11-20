import pygame
from random import choice, randint

pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))


# Subclass Apple inheriting from GameObject
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()  # Call reset here!

    def move(self):
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice([93, 218, 343])  # Randomly choose from three lanes
        self.y = -64


# Subclass Strawberry inheriting from GameObject
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx

        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice([50, 200, 350])


# Create instances of Apple and Strawberry
apples = [Apple() for _ in range(3)]  # Creating 3 apples
strawberries = [Strawberry() for _ in range(3)]  # Creating 3 strawberries

# Get the clock
clock = pygame.time.Clock()

# Create the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Move and render the apples and strawberries
    for apple in apples:
        apple.move()
        apple.render(screen)

    for strawberry in strawberries:
        strawberry.move()
        strawberry.render(screen)

    # Update the window
    pygame.display.flip()
    # Tick the clock!
    clock.tick(60)

pygame.quit()
