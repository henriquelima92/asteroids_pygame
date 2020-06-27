import pygame

_is_running = True

def _update():
    pass

def _draw(screen):
    pass

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

    pygame.init()
    _screen = pygame.display.set_mode([800,600])

    _game_loop()
    