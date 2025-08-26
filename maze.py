import pygame, random

class Maze:
    def __init__(self, cols=20, rows=15, cell_size=40):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.maze = [[1] * cols for _ in range(rows)]  # filled walls

        self.grid = [[{"visited": False, "walls": [True, True, True, True]}
                      for _ in range(cols)] for _ in range(rows)]

        self.generate_maze(0, 0)

        self.exit_pos = (cols - 1, rows - 1)

    def generate_maze(self, cx, cy):
        """Recursive backtracking algorithm"""
        self.grid[cy][cx]["visited"] = True

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < self.cols and 0 <= ny < self.rows and not self.grid[ny][nx]["visited"]:
                # Knock down walls between current and next
                if dx == 1:  # right
                    self.grid[cy][cx]["walls"][1] = False
                    self.grid[ny][nx]["walls"][3] = False
                if dx == -1:  # left
                    self.grid[cy][cx]["walls"][3] = False
                    self.grid[ny][nx]["walls"][1] = False
                if dy == 1:  # down
                    self.grid[cy][cx]["walls"][2] = False
                    self.grid[ny][nx]["walls"][0] = False
                if dy == -1:  # up
                    self.grid[cy][cx]["walls"][0] = False
                    self.grid[ny][nx]["walls"][2] = False

                self.generate_maze(nx, ny)

    def draw(self, screen):
        """Draw maze walls"""
        for y in range(self.rows):
            for x in range(self.cols):
                walls = self.grid[y][x]["walls"]
                px, py = x * self.cell_size, y * self.cell_size

                if walls[0]:  # top
                    pygame.draw.line(screen, (255, 255, 255), (px, py), (px + self.cell_size, py), 2)
                if walls[1]:  # right
                    pygame.draw.line(screen, (255, 255, 255), (px + self.cell_size, py),
                                     (px + self.cell_size, py + self.cell_size), 2)
                if walls[2]:  # bottom
                    pygame.draw.line(screen, (255, 255, 255), (px, py + self.cell_size),
                                     (px + self.cell_size, py + self.cell_size), 2)
                if walls[3]:  # left
                    pygame.draw.line(screen, (255, 255, 255), (px, py), (px, py + self.cell_size), 2)
