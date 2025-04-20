import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    dt = 0
    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill(color=(0,0,0))    
        player.draw(screen)
        pygame.display.flip()
        delta_milliseconds = clock.tick(60)
        dt = delta_milliseconds / 1000



if __name__ == "__main__":
    main()