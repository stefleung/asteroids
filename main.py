# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *  
from asteroidfield import * 
from shot import *


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for member in updatable:
            member.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                exit("Game over!")  

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0,0,0))

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()