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
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))


# Apple class, inherits from GameObject
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dy = 2  # Initial speed
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
        
    def increase_speed(self, increment):
        self.dy += increment


# Strawberry class, inherits from GameObject
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dy = 2  # Initial speed
        self.direction = choice([-1, 1])
        self.reset()

    def move(self):
        if self.direction == -1:
            self.x -= self.dy
        else:
            self.x += self.dy

        if self.x < -64 or self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64 if self.direction == 1 else 500
        self.y = choice(lanes)
        self.direction = choice([-1, 1])
        
    def increase_speed(self, increment):
        self.dy += increment


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
        self.dx = 2  # Initial speed
        self.dy = 2  # Initial speed
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
        direction = choice(['up', 'down', 'left', 'right'])
        self.direction = direction

        if direction == 'up':
            self.x = randint(0, 500)
            self.y = 500
        elif direction == 'down':
            self.x = randint(0, 500)
            self.y = -64
        elif direction == 'left':
            self.x = 500
            self.y = randint(0, 500)
        elif direction == 'right':
            self.x = -64
            self.y = randint(0, 500)


# Create instances of Apple, Strawberry, Player, and Bomb
apples = [Apple() for _ in range(3)]
strawberries = [Strawberry() for _ in range(3)]
player = Player()
bomb = Bomb()

# Make a group
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# Add player and bomb to all_sprites group
all_sprites.add(player)
all_sprites.add(bomb)

# Add individual apples and strawberries to fruit_sprites group
for apple in apples:
    fruit_sprites.add(apple)

for strawberry in strawberries:
    fruit_sprites.add(strawberry)

# Get the clock
clock = pygame.time.Clock()

# Lanes
lanes = [93, 218, 343]

# Create a variable to track player's score
player_score = 0


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    screen.fill((255, 255, 255))  # Clear the screen

    # Move and render all sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Move and render fruit sprites
    for fruit in fruit_sprites:
        fruit.move()
        fruit.render(screen)

    # Check for collisions between player and fruit sprites
    fruit_collision = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit_collision:
        fruit_collision.reset()
        player_score += 1
        # Increase the speed of fruits
        for fruit in fruit_sprites:
            fruit.dy += 0.5  # Increment the speed

    # Check collision between player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        # Reset game objects
        player_score = 0
        for fruit in fruit_sprites:
            fruit.dy = 2  # Reset fruit speed
            fruit.reset()
        bomb.reset()
        player.reset()

    pygame.display.flip()  # Update the window
    clock.tick(60)  # Control frame rate

pygame.quit()
