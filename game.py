import pygame
from player import Player
from npc import NPC
import time
from key import Key
from gate import Gate
from maze import Maze

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (30, 30, 30)
        self.player = Player(100, 100)
        self.key = Key(300, 150)
        self.gate = Gate(700, 250)
        self.has_key = False

        self.npcs = [
            NPC("Guide", 400, 300, personality="wise"),
            NPC("Joker", 200, 400, personality="funny")
        ]

        self.dialogue_text = ""
        self.font = pygame.font.SysFont("arial", 20)
        self.font_big = pygame.font.SysFont("arial", 28)

        self.talking_to = None
        self.last_dialogue_time = 0

        self.state = "main"  # main | maze | returning

        self.teleport_zone = pygame.Rect(self.gate.rect.topleft, self.gate.rect.size)
        self.show_teleport_prompt = False

        self.return_time = 0
        self.show_return_msg = False


    def update(self):
        # State-based update
        if self.state == "main":
            self.update_main()
        elif self.state == "maze":
            self.update_maze()
        elif self.state == "returning":
            self.update_returning()

        # NPC interaction (only during main state)
        if self.state in ["main", "returning"]:
            if self.talking_to is None:
                for npc in self.npcs:
                    if self.player.rect.colliderect(npc.rect):
                        self.dialogue_text = npc.talk()
                        self.talking_to = npc
                        self.last_dialogue_time = time.time()
                        break
            else:
                if not self.player.rect.colliderect(self.talking_to.rect):
                    self.dialogue_text = ""
                    self.talking_to = None

    def draw(self):
        self.screen.fill(self.bg_color)
        
        if self.state == "main" or self.state == "returning":
            self.player.draw(self.screen)
            for npc in self.npcs:
                npc.draw(self.screen, self.show_return_msg)

            self.key.draw(self.screen)
            self.gate.draw(self.screen)

            # ✅ Show purple portal where gate was
            if not self.gate.locked:
                pygame.draw.rect(self.screen, (100, 0, 200), self.teleport_zone, 3)

            if self.dialogue_text:
                self.draw_dialog_box(self.dialogue_text)

            if self.show_teleport_prompt:
                prompt = self.font_big.render("Press [E] to enter the portal", True, (255, 255, 255))
                self.screen.blit(prompt, (200, 540))

        elif self.state == "maze":
            self.maze.draw(self.screen)
            self.player.draw(self.screen)






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


    def update_main(self):
        self.player.move()

        # Key Pickup
        if self.key.check_pickup(self.player.rect):
            self.has_key = True

        self.gate.check_unlock(self.has_key)

        if self.gate.blocks_player(self.player.rect):
            if self.player.rect.right > self.gate.rect.left:
                self.player.rect.right = self.gate.rect.left

        # Show teleport prompt if gate is open
        self.show_teleport_prompt = False
        if not self.gate.locked and self.teleport_zone.colliderect(self.player.rect):
            self.show_teleport_prompt = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                self.load_maze()
                self.show_teleport_prompt = False   # ✅ fix: reset prompt



    def load_maze(self):
        self.state = "maze"
        self.maze = Maze()
        self.player.rect.topleft = (0, 0)


    def update_maze(self):
        keys = pygame.key.get_pressed()
        cell_x = self.player.rect.x // self.maze.cell_size
        cell_y = self.player.rect.y // self.maze.cell_size
        walls = self.maze.grid[cell_y][cell_x]["walls"]

        speed = self.player.speed
        moved = False

        if keys[pygame.K_UP] and not walls[0]:
            self.player.rect.y -= speed
            moved = True
        if keys[pygame.K_DOWN] and not walls[2]:
            self.player.rect.y += speed
            moved = True
        if keys[pygame.K_LEFT] and not walls[3]:
            self.player.rect.x -= speed
            moved = True
        if keys[pygame.K_RIGHT] and not walls[1]:
            self.player.rect.x += speed
            moved = True

        # Check if player reached exit
        if (cell_x, cell_y) == self.maze.exit_pos:
            self.state = "returning"
            self.player.rect.topleft = (100, 100)
            self.return_time = pygame.time.get_ticks()



    def update_returning(self):
        self.update_main()

        # Show greeting above NPCs for 5 seconds
        if pygame.time.get_ticks() - self.return_time < 5000:
            self.show_return_msg = True
        else:
            self.show_return_msg = False
            self.state = "main"
