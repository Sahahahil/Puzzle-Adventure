import pygame
import random

class Bush:
    def __init__(self, x, y, size=40):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = (34, 139, 34)  # forest green
        self.hidden_key = False  # by default no key

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 100, 0), self.rect, 2)  # dark outline
