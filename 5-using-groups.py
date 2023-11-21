import pygame
from random import randint, choice

# Initialize pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Define lanes
lanes = [93, 218, 343]


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
        self.direction = choice([-1, 1])
        self.reset()

    def move(self):
        self.y += self.dy * self.direction
        if (self.direction == -1 and self.y < -64) or (self.direction == 1 and self.y > 500):
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = -64 if self.direction == 1 else 500
        self.direction = choice([-1, 1])


# Strawberry class, inherits from GameObject
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = 2
        self.direction = choice([-1, 1])

    def move(self):
        self.x += self.dx * self.direction
        if (self.direction == 1 and self.x > 500) or (self.direction == -1 and self.x < -64):
            self.reset()

    def reset(self):
        self.x = -64 if self.direction == 1 else 500
        self.y = choice(lanes)
        self.direction = choice([-1, 1])


# Player class, inherits from GameObject
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(
            choice(lanes), choice(lanes), 'player.png')
        self.dx = self.x
        self.dy = self.y
        self.pos_x = lanes.index(self.x)
        self.pos_y = lanes.index(self.y)

    def move(self):
        self.x = self.dx
        self.y = self.dy

        if self.dx not in lanes:
            closest_x = min(lanes, key=lambda vx: abs(vx - self.dx))
            self.dx = closest_x

        if self.dy not in lanes:
            closest_y = min(lanes, key=lambda vy: abs(vy - self.dy))
            self.dy = closest_y

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()


# Bomb class, inherits from GameObject
class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        self.dx = 2
        self.dy = 2
        self.direction = choice(['up', 'down', 'left', 'right'])
        self.reset()

    def move(self):
        if self.direction == 'up':
            self.y -= self.dy
        elif self.direction == 'down':
            self.y += self.dy
        elif self.direction == 'left':
            self.x -= self.dx
        elif self.direction == 'right':
            self.x += self.dx

        # Check if the Bomb is out of the screen, then reset
        if self.x < -64 or self.x > 500 or self.y < -64 or self.y > 500:
            self.reset()

    def reset(self):
        self.x = randint(50, 450)
        self.y = randint(50, 450)
        self.direction = choice(['up', 'down', 'left', 'right'])


# Create instances of Apple, Strawberry, Player, and Bomb
apples = [Apple() for _ in range(3)]
strawberries = [Strawberry() for _ in range(3)]
player = Player()
bomb = Bomb()

# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(*apples)
all_sprites.add(*strawberries)
all_sprites.add(bomb)

# Get the clock
clock = pygame.time.Clock()

# Lanes
lanes = [93, 218, 343]

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

    # Move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Update the window
    pygame.display.flip()
    # Tick the clock!
    clock.tick(60)

pygame.quit()
