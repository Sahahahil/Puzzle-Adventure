import pygame
import random

class Maze:
    def __init__(self, cols=10, rows=10):
        self.cols = cols
        self.rows = rows
        self.cell_size = 50
        self.maze = [[1 for _ in range(cols)] for _ in range(rows)]
        self.generate_maze()

        self.exit_pos = (cols - 1, rows - 1)

    def generate_maze(self):
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        def dfs(x, y):
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            random.shuffle(dirs)
            visited[y][x] = True
            self.maze[y][x] = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.cols and 0 <= ny < self.rows and not visited[ny][nx]:
                    self.maze[y + dy//2][x + dx//2] = 0
                    dfs(nx, ny)

        dfs(0,0)

    def draw(self, screen):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                color = (50, 50, 50) if self.maze[y][x] == 1 else (200, 200, 200)
                pygame.draw.rect(screen, color, rect)
        # Draw exit
        pygame.draw.rect(screen, (0, 255, 0), (self.exit_pos[0]*self.cell_size, self.exit_pos[1]*self.cell_size, self.cell_size, self.cell_size))
