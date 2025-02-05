from constants import *

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        
        
if __name__ == "__main__":
    main()
