import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(x,y)
    dt = 0
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroid = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)

    

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                sys.exit(0)
        for a in asteroids:
            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()
        screen.fill(color=(0,0,0))  
        for d in drawable:
            d.draw(screen)  
        pygame.display.flip()
        delta_milliseconds = clock.tick(60)
        dt = delta_milliseconds / 1000



if __name__ == "__main__":
    main()