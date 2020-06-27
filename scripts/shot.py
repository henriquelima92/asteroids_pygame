import pygame
from scripts import constant
from scripts.utilities import Vector2


class Shot(object):

    def __init__(self, position, direction):
        self.position = Vector2(position.x,position.y)
        self.direction = direction
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load(constant.SPRITES_FOLDER + "shot.png")
        self.sprite.image = pygame.transform.scale(self.sprite.image, (10, 30))
        self.rect = self.sprite.image.get_rect() 
        self.rect.center = (40 / 2, 40 / 2 )

    def update(self):
        self.position.x += self.direction.x
        self.position.y += self.direction.y

    def draw(self, screen):
        screen.blit(self.sprite.image, self.position.get_vector2())
