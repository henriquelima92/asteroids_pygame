import pygame
from scripts.utilities import Vector2

class Player(object):
    def __init__(self):
        self.position = Vector2(50, 440)
        self.size = Vector2(1,1)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("sprites/player.png")
        self.sprite.rect = self.sprite.image.get_rect()
        

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.position.x -= 1
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.position.x += 1

    def _check_borders(self):
        pass

    def draw(self, screen):
        screen.blit(self.sprite.image, self.position.get_vector2())

    def destroy(self):
        pass
