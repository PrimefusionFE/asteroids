import pygame
from pygame.locals import *
from constants import *



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)

def game_loop(screen):
    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        handle_input(screen)

        update(screen)

        render(screen)

        dt = (clock.tick(fps) / 1000)

def handle_input(screen):
    pass

def update(screen):
    pass

def render(screen):
    screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
    main()
