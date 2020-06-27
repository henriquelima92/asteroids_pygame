import pygame
from scripts import constant
from scripts.utilities import Vector2, Collider
from scripts.shot import Shot

class Player(object):
    

    def __init__(self):
        self.position = Vector2(50, 440)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load(constant.SPRITES_FOLDER + "player.png")
        self.sprite.image = pygame.transform.scale(self.sprite.image, (40, 40))
        self.rect = self.sprite.image.get_rect() 
        self.rect.center = (40 / 2, 40 / 2 )
        
        self.collider = Collider(self.position.x, self.position.y)
        self.shots = []
        
    def inputs(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shot()


    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.position.x -= 1
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.position.x += 1

        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            self.position.y -= 1
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            self.position.y += 1

        if len(self.shots) > 0:
            for shot in self.shots:
                shot.update()

        self._check_borders()

    def shot(self):
        new_shot = Shot(self.position, Vector2(0,-1))
        self.shots.append(new_shot)

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
        screen.blit(self.sprite.image, self.position.get_vector2())
        if len(self.shots) > 0:
            for shot in self.shots:
                shot.draw(screen)

    def destroy(self):
        pass
