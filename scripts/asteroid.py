import pygame
import random
from scripts import constant
from pygame.math import Vector2
import math

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, position, scale):
        super(Asteroid, self).__init__()
        self.scale = scale
        self.surf = pygame.Surface(self.scale)
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.position = position
        self.speed = 0.5

        self.speedx = (random.randrange(1)*2-1)*((random.randrange(70)+5))/(80 + 30 * self.scale.x) * math.cos(random.randrange(0,360))
        self.speedy = (random.randrange(1)*2-1)*((random.randrange(70)+5))/(80 + 30 * self.scale.y) * math.sin(random.randrange(0,360))
        

    def update(self):
        self.position.x += 50 * self.speedx / (self.scale.x + 1)
        self.position.y += 50 * self.speedy / (self.scale.y + 1)

        self._check_borders()

    def draw(self, screen):
        screen.blit(self.surf, self.position)

    def _check_borders(self):
        if self.position.x > constant.SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = constant.SCREEN_WIDTH

        if self.position.y > constant.SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = constant.SCREEN_HEIGHT

    def _reset(self):
        self.position.y = 0
        self.position.x = random.randint(0, 560)