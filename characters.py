import pygame
from random import choice, randint
from sprites import GameObject

lanes = [50, 150, 250, 350, 450, 550]

# Player class, inherits from GameObject
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(350, 250, 'images/astronaut.png')
        self.dx = self.x
        self.dy = self.y
        self.pos_x = lanes.index(self.x)
        self.pos_y = lanes.index(self.y)
        self.movement_step = 4  # Increase the movement step size

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
                # Limit movement within the left boundary of the screen
                if self.dx < 0:
                    self.dx = max(self.dx, 0)

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()
            # Limit movement within the right boundary of the screen
            if self.dx > 750 - self.rect.width:  # Assuming width of the astronaut sprite
                self.dx = min(self.dx, 750 - self.rect.width)

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()
            # Limit movement within the upper boundary of the screen
            if self.dy < 0:
                self.dy = max(self.dy, 0)

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()
            # Limit movement within the lower boundary of the screen
            if self.dy > 500 - self.rect.height:  # Assuming height of the astronaut sprite
                self.dy = min(self.dy, 500 - self.rect.height)


# Alien class, inherits from GameObject
class Alien(GameObject):
    def __init__(self):
        super(Alien, self).__init__(0, 0, 'images/alien.png')
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

        # Check if the Alien is out of the screen, then reset
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