import pygame
from random import choice

pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Base class for game objects
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

# Apple class, inherits from GameObject
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dy = 2
        self.reset()

    def move(self):
        self.y += self.dy
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice([93, 218, 343])
        self.y = -64

# Strawberry class, inherits from GameObject
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = 2
        self.reset()

    def move(self):
        self.x += self.dx
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice([50, 200, 350])

# Player class, inherits from GameObject
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(choice([93, 218, 343]), choice([50, 200, 350]), 'player.png')
        self.dx = self.x
        self.dy = self.y

        # Valid intersections where the player can move
        self.valid_x = [93, 218, 343]
        self.valid_y = [50, 200, 350]

    def move(self):
        self.x = self.dx
        self.y = self.dy

        if self.dx not in self.valid_x:
            closest_x = min(self.valid_x, key=lambda vx: abs(vx - self.dx))
            self.dx = closest_x

        if self.dy not in self.valid_y:
            closest_y = min(self.valid_y, key=lambda vy: abs(vy - self.dy))
            self.dy = closest_y

    def left(self):
        current_index = self.valid_x.index(self.x)
        if current_index > 0:
            self.dx = self.valid_x[current_index - 1]

    def right(self):
        current_index = self.valid_x.index(self.x)
        if current_index < len(self.valid_x) - 1:
            self.dx = self.valid_x[current_index + 1]

    def up(self):
        current_index = self.valid_y.index(self.y)
        if current_index > 0:
            self.dy = self.valid_y[current_index - 1]

    def down(self):
        current_index = self.valid_y.index(self.y)
        if current_index < len(self.valid_y) - 1:
            self.dy = self.valid_y[current_index + 1]


# Create instances of Apple, Strawberry, and Player
apples = [Apple() for _ in range(3)]
strawberries = [Strawberry() for _ in range(3)]
player = Player()

# Get the clock
clock = pygame.time.Clock()

# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # Clear screen
    screen.fill((255, 255, 255))

    # Move and render the apples and strawberries
    for apple in apples:
        apple.move()
        apple.render(screen)

    for strawberry in strawberries:
        strawberry.move()
        strawberry.render(screen)

    # Draw player
    player.move()
    player.render(screen)

    # Update the window
    pygame.display.flip()
    # Tick the clock!
    clock.tick(60)

pygame.quit()
