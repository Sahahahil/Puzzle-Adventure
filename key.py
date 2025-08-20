import pygame

class Key:
    def __init__(self, x, y):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 215, 0))  # Gold color
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)

    def check_pickup(self, player_rect):
        if not self.collected and self.rect.colliderect(player_rect):
            self.collected = True
            return True
        return False
