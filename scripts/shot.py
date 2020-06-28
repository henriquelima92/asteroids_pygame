import pygame
from scripts import constant
from pygame.math import Vector2
import math

class Shot(pygame.sprite.Sprite):

    def __init__(self, position, angle):
        super(Shot, self).__init__()
        self.scale = Vector2(5,5)
        self.surf = pygame.Surface(self.scale)
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect()
        self.position = position

        if angle + 90 > 360:
            angle -= 360.0

        self.real_angle = math.radians(angle + 90)
        self.speedx = +1.0 * math.cos(self.real_angle)
        self.speedy = -1.0 * math.sin(self.real_angle)

        self.speed = 1

    def update(self):
        self.position.x += self.speedx
        self.position.y += self.speedy

    def draw(self, screen):
        screen.blit(self.surf, self.position)
