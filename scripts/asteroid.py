import pygame
import random
from scripts import constant
from pygame.math import Vector2
import math

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, _start_position, _type):
        super(Asteroid, self).__init__()
        self.type = _type
        self.position = _start_position

        self.scale = self._get_scale()

        self.surf = pygame.Surface(self.scale)
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()

        self.speed = self._get_speed() 
        self.angle = self._get_angle()
        self.direction = self._get_movement_direction()

    def _get_speed(self):    
        if self.type == 1:
            return random.uniform(0.11,0.14)
        elif self.type == 2:
            return random.uniform(0.08,0.10)
        elif self.type == 3:
            return random.uniform(0.05,0.07)
        else:
            return random.uniform(0.02,0.04)    

    def _get_angle(self):
        return random.randrange(0,360)

    def _get_movement_direction(self):
        direction_x = self.speed * math.sin(self.angle)
        direction_y = self.speed * math.cos(self.angle)

        return Vector2(direction_x, direction_y)

    def _get_scale(self):
        if self.type == 1:
            return Vector2(15,15)
        elif self.type == 2:
            return Vector2(30,30)
        elif self.type == 3:
            return Vector2(45,45)
        else:
            return Vector2(60,60)

    def _check_borders(self):
        if self.position.x > constant.SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = constant.SCREEN_WIDTH

        if self.position.y > constant.SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = constant.SCREEN_HEIGHT


    def update(self):
        self.position += self.direction

        self._check_borders()

    def draw(self, screen):
        screen.blit(self.surf, self.position)

    