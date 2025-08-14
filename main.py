import pygame
from pygame.locals import *
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")    
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    fps = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        handle_input(screen)

        update(dt, updatable)

        render(screen, drawable)

        dt = (clock.tick(fps) / 1000)

def handle_input(screen):
    pass

def update(dt, group):
    for member in group:
        member.update(dt)

def render(screen, group):
    screen.fill("black")

    for member in group:
        member.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
    main()
