import pygame
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, projectiles)

    #asteroid = Asteroid(0, 39, 4)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidf = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    for u in updatable:
        print(u)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
       
        updatable.update(dt)
        for aster in asteroids:
            if aster.is_colliding(player):
                print("Game over!")
                sys.exit()
            for p in projectiles:
                if aster.is_colliding(p):
                    aster.split()
                    p.kill()
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
