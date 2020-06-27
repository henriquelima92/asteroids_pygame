import pygame
import random
from scripts import constant
from scripts.utilities import Vector2, Collider

class Asteroid(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, 560), 0)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load(constant.SPRITES_FOLDER + "asteroid_0.png")
        self.sprite.image = pygame.transform.scale(self.sprite.image, (30, 30))
        self.rect = self.sprite.image.get_rect() 
        self.rect.center = (30 / 2, 30 / 2 )
        
        self.collider = Collider(self.position.x, self.position.y)

    def update(self):
        self.position.y += 0.4
        if self.position.y > constant.SCREEN_HEIGHT:
            self._reset()

    def draw(self, screen):
        screen.blit(self.sprite.image, self.position.get_vector2())

    def _reset(self):
        self.position.y = 0
        self.position.x = random.randint(0, 560)