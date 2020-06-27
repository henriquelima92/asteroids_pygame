import pygame
from scripts.utilities import Vector2

class Player(object):
    def __init__(self, screen_w, screen_h):
        global _screen

        self.position = Vector2(50, 440)
        self.size = Vector2(1,1)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("sprites/player.png")
        self.sprite.rect = self.sprite.image.get_rect()
        _screen = [screen_w, screen_h]
        

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.position.x -= 1
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.position.x += 1

        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            self.position.y -= 1
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            self.position.y += 1

        self._check_borders()

    def _check_borders(self):
        if self.position.x > _screen[0]:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = _screen[0]

        if self.position.y > _screen[1]:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = _screen[1]

    def draw(self, screen):
        screen.blit(self.sprite.image, self.position.get_vector2())

    def destroy(self):
        pass
