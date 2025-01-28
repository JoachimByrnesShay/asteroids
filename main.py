import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
  
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.Surface.fill(screen, (0,0,0))
        for toUpdate in updatable:
            toUpdate.update(dt)
        # player.update(dt)
        screen.fill("black")
        for toDraw in drawable:
            toDraw.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
   # print("Starting asteroids!")
  


if __name__ == "__main__":
    main()