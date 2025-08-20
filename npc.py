import pygame
import random

class NPC:
    def __init__(self, name, x, y, personality="neutral"):
        self.name = name
        self.personality = personality
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.dialogues = {
            "wise": [
                "The door opens only for those who ask the right questions.",
                "Seek the stone that glows in moonlight.",
                "Sometimes silence is the best answer.",
                "Have you found the golden key? It open what is locked."
            ],
            "funny": [
                "Why did the wizard cross the road? No one knows!",
                "I’d help you, but I left my clue in my other robe.",
                "I speak in riddles… or do I?"
            ],
            "neutral": [
                "Hello, traveler.",
                "Good luck on your quest.",
                "It's quiet here... too quiet."
            ]
        }

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def talk(self):
        return f"{self.name}: {random.choice(self.dialogues[self.personality])}"

    def draw(self, screen, show_return_msg=False):
        screen.blit(self.image, self.rect)
        if show_return_msg:
            font = pygame.font.SysFont("arial", 20)
            text = font.render("You are back!", True, (255, 255, 0))
            screen.blit(text, (self.rect.x, self.rect.y - 25))
