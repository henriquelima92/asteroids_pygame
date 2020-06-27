import pygame
import random
from scripts import constant
from scripts.utilities import Vector2, Collider

WIDTH = 30
HEIGHT = 30

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.surf = pygame.Surface((WIDTH,HEIGHT))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.position = Vector2(random.randint(0, 560), 0)
        self.speed = 0.5
        
        self.collider = Collider(self.position.x, self.position.y)

    def update(self):
        self.position.y += self.speed
        if self.position.y > constant.SCREEN_HEIGHT:
            self._reset()

    def draw(self, screen):
        screen.blit(self.surf, self.position.get_vector2())

    def _reset(self):
        self.position.y = 0
        self.position.x = random.randint(0, 560)