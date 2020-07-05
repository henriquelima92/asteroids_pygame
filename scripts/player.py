import pygame
from scripts import constant
from scripts.shot import Shot
from pygame.math import Vector2
import math

from scripts.collider import Collider




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.enemy = enemy
        self.scale = Vector2(40, 40)
        self.surf = pygame.Surface(self.scale, pygame.SRCALPHA)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.position = Vector2(constant.SCREEN_WIDTH/2, constant.SCREEN_HEIGHT/2)

        self.collider = Collider(self.position, self.scale)
        
        self.acceleration = 0.015
        self.rotation_speed = 0.7
        self.angle = 0
        self.current_speed = Vector2(0,0)

        self.is_alive = True
        self.shots = []

        self.hitbox = (self.position.x, self.position.y, self.scale.x, self.scale.y)
        
    def inputs(self, event):
        if self.is_alive == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shot()

    def _left(self):
        self.angle += self.rotation_speed
        if self.angle > 360.0:
            self.angle -= 360.0

    def _right(self):
        self.angle -= self.rotation_speed
        if self.angle < 0.0:
            self.angle += 360.0

    def _up(self):
        self._accelerate(self.angle)

    def _accelerate(self, angle):
        self.current_speed = self._accelerate_speed(angle, self.current_speed[0], self.current_speed[1])

    def _accelerate_speed(self, angle, x, y):
        real_angle = angle + 90

        if real_angle > 360:
            real_angle -= 360.0
        real_angle *= math.pi / 180
        
        rady =- math.sin(real_angle)
        radx = math.cos(real_angle)

        if (rady < 0 and not y < -0.5) or (rady > 0 and not y > 0.5):
            y += rady * self.acceleration
        if (radx < 0 and not x < -0.5) or (radx > 0 and not x > 0.5):    
            x += radx * self.acceleration
        
        return x,y


    def update(self, asteroid_controller):
        for asteroid in asteroid_controller.asteroid_list:
            if self.collider.check_collision(self.position, asteroid):
                if self.is_alive == True:
                    self.is_alive = False
                    self.kill()
                    asteroid_controller.remove_asteroid(asteroid)

        if self.is_alive == True:
            if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
                self._left()
            elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
                self._right()
            
            if pygame.key.get_pressed()[pygame.K_UP] != 0:
                self._up()

            self.position += self.current_speed

            if len(self.shots) > 0:
                for shot in self.shots:
                    shot.update(asteroid_controller)

            self._check_borders()

    def check_collision(self):
        if self.position.x < self.enemy.position.x + self.enemy.scale.x and self.position.x + self.scale.x > self.enemy.position.x and self.position.y < self.enemy.position.y + self.enemy.scale.y and self.position.y + self.scale.y > self.enemy.position.y:
            if self.is_alive == True:
                self.is_alive = False
                print("entrou")

    def shot(self):
        new_shot = Shot(self._get_shot_position(), self.angle, self.shots)
        self.shots.append(new_shot)

    def _get_shot_position(self):
        return Vector2(self.position.x, self.position.y)

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
        if self.is_alive == True:
            player_surface = pygame.transform.rotate(self.surf, self.angle)
            player_rect = player_surface.get_rect()
            player_rect.center = self.position
            screen.blit(player_surface, player_rect)

            self.hitbox = (self.position.x - (self.scale.x/2), self.position.y - (self.scale.y/2), self.scale.x, self.scale.y)
            if constant.DEBUG_MODE == True:
                pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

            if len(self.shots) > 0:
                for shot in self.shots:
                    shot.draw(screen)

    def destroy(self):
        pass
