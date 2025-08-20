import pygame
import sys
from game import Game

#initialize game
pygame.init()

#game window
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Puzzle Adventure")

#game clock
clock = pygame.time.Clock()

#game object
game = Game(SCREEN)

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.update()
    game.draw()

    pygame.display.update()
    clock.tick(60)