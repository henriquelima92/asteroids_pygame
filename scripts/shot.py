import pygame
from scripts import constant
from pygame.math import Vector2

class Shot(pygame.sprite.Sprite):

    def __init__(self, position, direction):
        super(Shot, self).__init__()
        self.scale = Vector2(3,10)
        self.surf = pygame.Surface(self.scale)
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect()
        self.position = position
        self.direction = direction
        self.speed = 1

    def update(self):
        self.position.x += (self.direction.x * self.speed)
        self.position.y += (self.direction.y * self.speed)

    def draw(self, screen):
        screen.blit(self.surf, self.position)
