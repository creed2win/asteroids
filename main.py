import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    test = ['*', ' ', 'E', 'n', 'd', 'e', 'r', ' ', 'W', 'i', 'g', 'g', 'i', 'n']

    joined_test = ''.join(test)

    print(joined_test)

    pygame.init()

    pyClock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("#6e6e6e")

        player.draw(screen)
        
        pygame.display.flip()
        

        dt = pyClock.tick(60)

        
if __name__ == "__main__":
    main()


