import pygame
from scripts.player import Player
from scripts.asteroid import Asteroid
from scripts import constant
from pygame.math import Vector2

_is_running = True

enemies_group = pygame.sprite.Group()
character_group = pygame.sprite.Group()

enemies_list = []
shots_list = []


def _update():
    _player.update()
    _asteroid.update()
    _asteroid2.update()
    pass

def _draw(screen):
    screen.fill([0, 0, 0])
    
    _player.draw(screen)
    _asteroid.draw(screen)
    _asteroid2.draw(screen)

    pygame.display.update()

def _inputs():
    global _is_running
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _is_running = False
            _player.inputs(event)

def _game_loop():

    while _is_running == True:
        _inputs()
        _update()
        _draw(_screen)

    pygame.quit()


if __name__ == '__main__':
    global _screen
    global _player

    pygame.init()
    _screen = pygame.display.set_mode([constant.SCREEN_WIDTH,constant.SCREEN_HEIGHT])
    _asteroid = Asteroid(Vector2(400, 300))
    _asteroid2 = Asteroid(Vector2(45,15))
    _player = Player(_asteroid)
    
    character_group.add(_player)
    enemies_group.add(_asteroid)

    _game_loop()
    