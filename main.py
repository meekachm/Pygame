import pygame
from sprites import Star, Strawberry, MeteorBackground
from characters import Player, Alien

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([750, 500])
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('images/space_bg.jpg').convert()
        self.lanes = [50, 150, 250, 350, 450, 550]
        self.setup_game()

    def setup_game(self):
        self.player = Player()
        self.alien = Alien()
        self.stars = [Star() for _ in range(3)]
        self.strawberries = [Strawberry() for _ in range(3)]
        self.meteors = [MeteorBackground() for _ in range(3)]
        self.all_sprites = pygame.sprite.Group()
        self.fruit_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.player, self.alien)
        self.fruit_sprites.add(*self.stars, *self.strawberries)
        self.all_sprites.add(*self.meteors, *self.stars, *self.strawberries)

        self.player_score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    self.handle_player_movement(event.key)
        return True

    def handle_player_movement(self, key):
        if key == pygame.K_LEFT:
            self.player.left()
        elif key == pygame.K_RIGHT:
            self.player.right()
        elif key == pygame.K_UP:
            self.player.up()
        elif key == pygame.K_DOWN:
            self.player.down()

    def update_game(self):
        for entity in self.all_sprites:
            entity.move()
            entity.render(self.screen)

        fruit_collision = pygame.sprite.spritecollideany(self.player, self.fruit_sprites)
        if fruit_collision:
            fruit_collision.reset()
            self.player_score += 1

        if pygame.sprite.collide_rect(self.player, self.alien):
            self.player_score = 0
            for fruit in self.fruit_sprites:
                fruit.dy = 2  # Reset fruit speed
                fruit.reset()
            self.alien.reset()
            self.player.reset()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.screen.blit(self.background, (0, 0))
            self.update_game()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
