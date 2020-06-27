import pygame
from scripts.player import Player
from scripts.asteroid import Asteroid
from scripts import constant

_is_running = True

def _update():
    _player.update()
    _asteroid.update()
    pass

def _draw(screen):
    screen.fill([0, 0, 0])
    
    _player.draw(screen)
    _asteroid.draw(screen)

    pygame.display.update()

def _inputs():
    global _is_running

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _is_running = False

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
    _player = Player()
    _asteroid = Asteroid()

    _game_loop()
    