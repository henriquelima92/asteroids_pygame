import pygame
from scripts.player import Player


_is_running = True

def _update():
    _player.update()
    pass

def _draw(screen):
    screen.fill([0, 0, 0])
    _player.draw(screen)
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
    _screen = pygame.display.set_mode([800,600])
    _player = Player()

    _game_loop()
    