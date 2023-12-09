import pygame
from random import randint, choice

# Lanes
lanes = [50, 150, 250, 350, 450, 550]

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


# Star class, inherits from GameObject
class Star(GameObject):
    def __init__(self):
        super(Star, self).__init__(0, 0, 'images/star.png')
        self.dy = 1.5  # Initial speed
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
        super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
        self.dy = 1.5  # Initial speed
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


# MeteorBackground class, inherits from GameObject
class MeteorBackground(GameObject):
    def __init__(self):
        super(MeteorBackground, self).__init__(0, 0, 'images/meteor.png')
        self.dx = 0.3  # Initial speed
        self.reset()

    def move(self):
        self.x += self.dx
        if self.x > 750:  
            self.reset()

    def reset(self):
        self.x = -64
        self.y = randint(0, 500) 






