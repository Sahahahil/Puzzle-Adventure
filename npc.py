import pygame
import random

class NPC:
    def __init__(self, name, x, y, personality="neutral"):
        self.name = name
        self.personality = personality
        self.rect = pygame.Rect(x, y, 40, 40)  # Base size

        self.dialogues = {
            "wise": [
                "The door opens only for those who ask the right questions.",
                "Seek the stone that glows in moonlight.",
                "Sometimes silence is the best answer.",
                "Have you found the golden key? It opens what is locked."
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

    def talk(self):
        return f"{self.name}: {random.choice(self.dialogues[self.personality])}"

    def draw(self, screen, show_return_msg=False):
        cx, cy = self.rect.center
        radius = 20

        # Base circle (all NPCs have this)
        base_color = (0, 128, 255) if self.personality == "wise" else (200, 200, 50)
        pygame.draw.circle(screen, base_color, (cx, cy), radius)

        # Guide → Circle + Triangle hat
        if self.personality == "wise":
            triangle_points = [
                (cx, cy - radius - 12),
                (cx - 14, cy - radius + 4),
                (cx + 14, cy - radius + 4)
            ]
            pygame.draw.polygon(screen, (0, 200, 100), triangle_points)

        # Joker → Circle + Red dot nose
        elif self.personality == "funny":
            pygame.draw.circle(screen, (255, 0, 0), (cx, cy), 6)

        # NPC name above
        font = pygame.font.SysFont("arial", 16)
        name_surface = font.render(self.name, True, (255, 255, 255))
        screen.blit(name_surface, (self.rect.x, self.rect.y - 20))

        # Return message
        if show_return_msg:
            msg = font.render("You are back!", True, (255, 255, 0))
            screen.blit(msg, (self.rect.x - 10, self.rect.y - 35))
