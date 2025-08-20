import pygame
from player import Player
from npc import NPC

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (30, 30, 30)
        self.player = Player(100, 100)
        self.npcs = [
            NPC("Guide", 400, 300, personality="wise"),
            NPC("Joker", 200, 400, personality="funny")
        ]

    def update(self):
        self.player.move()

    def draw(self):
        self.screen.fill(self.bg_color)
        self.player.draw(self.screen)
        for npc in self.npcs:
            npc.draw(self.screen)

        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                npc.talk()