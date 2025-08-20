import pygame

class Gate:
    def __init__(self, x, y, width=60, height=100):
        self.locked = True
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100))  # Gray
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        if self.locked:
            screen.blit(self.image, self.rect)

    def check_unlock(self, has_key):
        if has_key:
            self.locked = False

    def blocks_player(self, player_rect):
        return self.locked and self.rect.colliderect(player_rect)
