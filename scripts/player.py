import pygame
from scripts import constant
from scripts.utilities import Collider
from scripts.shot import Shot
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.scale = Vector2(40, 40)
        self.surf = pygame.Surface(self.scale)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.position = Vector2(50, 440)
        self.speed = 0.7
        
        self.collider = Collider(self.position.x, self.position.y)
        self.shots = []
        
    def inputs(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shot()


    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.position.x -= self.speed
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.position.x += self.speed

        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            self.position.y -= self.speed
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            self.position.y += self.speed

        if len(self.shots) > 0:
            for shot in self.shots:
                shot.update()

        self._check_borders()

    def shot(self):
        new_shot = Shot(self._get_shot_position(), Vector2(0,-1))
        self.shots.append(new_shot)

    def _get_shot_position(self):
        return Vector2(self.position.x + self.scale.x/2, self.position.y - self.scale.y/2)

    def _check_borders(self):
        if self.position.x > constant.SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = constant.SCREEN_WIDTH

        if self.position.y > constant.SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = constant.SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.surf, self.position)

        if len(self.shots) > 0:
            for shot in self.shots:
                shot.draw(screen)

    def destroy(self):
        pass
