import pygame
from pygame.locals import *
from constants import *

MS_PER_UPDATE = 60

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    num_pass, num_fail = pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)

def game_loop(screen):
    previous_time = pygame.time.get_ticks()
    lag = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - previous_time
        previous_time= current_time
        lag += elapsed_time
    
        handle_input(screen)

        while lag >= MS_PER_UPDATE:
            update(screen)
            lag -= MS_PER_UPDATE

        render(screen)

def handle_input(screen):
    pass

def update(screen):
    pass

def render(screen):
    screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
    main()
