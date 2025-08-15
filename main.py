import pygame
from pygame.locals import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")    
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0
    fps = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        handle_input(screen)

        update(dt, updatable)

        if is_game_over(asteroids, player):
            print ("Game over!")
            return

        render(screen, drawable)

        dt = (clock.tick(fps) / 1000)

def handle_input(screen):
    pass

def update(dt, group):
    for member in group:
        member.update(dt)

def is_game_over(asteroids, player):
    for a in asteroids:
        if a.is_colliding(player):
            return True
    
    return False

def render(screen, group):
    screen.fill("black")

    for member in group:
        member.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
    main()
