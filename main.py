import pygame
from pygame.locals import *
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
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

        update(screen, dt, player)

        render(screen, player)

        dt = (clock.tick(fps) / 1000)

def handle_input(screen):
    pass

def update(screen, dt, player):
    player.update(dt)

def render(screen, player):
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
    main()
