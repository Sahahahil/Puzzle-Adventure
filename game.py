import pygame
from player import Player
from npc import NPC
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (30, 30, 30)
        self.player = Player(100, 100)
        self.npcs = [
            NPC("Guide", 400, 300, personality="wise"),
            NPC("Joker", 200, 400, personality="funny")
        ]
        self.dialogue_text = ""  # Store dialogue to show
        self.font = pygame.font.SysFont("arial", 20)

        self.talking_to = None 
        self.last_dialogue_time = 0

    def update(self):
        self.player.move()

        if self.talking_to is None:
            for npc in self.npcs:
                if self.player.rect.colliderect(npc.rect):
                    self.dialogue_text = npc.talk()
                    self.talking_to = npc
                    self.last_dialogue_time = time.time()
                    break
        else:
            # If player walks away, stop showing dialogue
            if not self.player.rect.colliderect(self.talking_to.rect):
                self.dialogue_text = ""
                self.talking_to = None

    def draw(self):
        self.screen.fill(self.bg_color)
        self.player.draw(self.screen)
        for npc in self.npcs:
            npc.draw(self.screen)

        if self.dialogue_text:
            self.draw_dialog_box(self.dialogue_text)

    def draw_dialog_box(self, text):
        box_width = 760
        box_height = 100
        box_x = 20
        box_y = 480
        pygame.draw.rect(self.screen, (0, 0, 0), (box_x, box_y, box_width, box_height))
        pygame.draw.rect(self.screen, (255, 255, 255), (box_x, box_y, box_width, box_height), 2)

        wrapped_text = self.wrap_text(text, self.font, box_width - 20)
        for i, line in enumerate(wrapped_text):
            line_surf = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(line_surf, (box_x + 10, box_y + 10 + i * 25))

    def wrap_text(self, text, font, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        lines.append(current_line.strip())
        return lines