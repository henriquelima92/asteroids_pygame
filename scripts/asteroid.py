import pygame
import random
from scripts import constant
from pygame.math import Vector2

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Asteroid, self).__init__()
        self.scale = Vector2(30,30)
        self.surf = pygame.Surface(self.scale)
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.position = position
        self.speed = 0.5
        

    def update(self):
        pass

        # self.position.y += self.speed
        # if self.position.y > constant.SCREEN_HEIGHT:
        #     self._reset()

    def draw(self, screen):
        screen.blit(self.surf, self.position)

    def _reset(self):
        self.position.y = 0
        self.position.x = random.randint(0, 560)