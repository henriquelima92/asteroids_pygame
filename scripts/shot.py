import pygame
from scripts import constant
from pygame.math import Vector2
from scripts.collider import Collider
import math

class Shot(pygame.sprite.Sprite):

    def __init__(self, position, angle, shots_list, asteroid_controller, highscore, audio):
        super(Shot, self).__init__()
        self.scale = Vector2(5,5)
        self.surf = pygame.Surface(self.scale)
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect()
        self.position = position
        self.shots_list = shots_list

        if angle + 90 > 360:
            angle -= 360.0

        self.real_angle = math.radians(angle + 90)
        self.speedx = +1.0 * math.cos(self.real_angle)
        self.speedy = -1.0 * math.sin(self.real_angle)

        self.speed = 1

        self.hitbox = (self.position.x, self.position.y, self.scale.x, self.scale.y)
        self.collider = Collider(self.hitbox)
        self.asteroid_controller = asteroid_controller
        self.highscore = highscore
        self.audio = audio

    def update(self):
        self.position.x += self.speedx
        self.position.y += self.speedy

        self._check_borders()

        for asteroid in self.asteroid_controller.asteroid_list:
            if self.collider.check_collision(self.position, asteroid) == True:
                self._kill_shot()
                self.highscore.increase_points(asteroid.type)
                self.asteroid_controller.remove_asteroid(asteroid)
                self.audio.play_asteroid_explosion()


    def _check_borders(self):
        if self.position.x < 0 or self.position.x > constant.SCREEN_WIDTH or self.position.y < 0 or self.position.y > constant.SCREEN_HEIGHT:
            self._kill_shot()

    def _kill_shot(self):
        if self in self.shots_list:
            self.shots_list.remove(self)
            del self

    def draw(self, screen):
        screen.blit(self.surf, self.position)
        self.hitbox = (self.position.x, self.position.y, self.scale.x, self.scale.y)

        if constant.DEBUG_MODE == True:
            pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
