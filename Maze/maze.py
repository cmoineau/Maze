from Maze.cell import cell
import pygame
from variables import *
from random import randint
from sys import exit

class MazeObject(object):
    def __init__(self, maze_size):
        self.w = maze_size[0]
        self.h = maze_size[1]
        self.grid = []
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.generate()

    def show_constrution(self):
        # clearing the screen
        self.window.fill(BLACK)
        for cell in self.grid:
            cell.show_constrution(self.window)
        # We update the canvas every time we draw a cell
        pygame.display.update()

    def show(self):
        for event in pygame.event.get():  # Checking event to exit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # clearing the screen
        self.window.fill(BLACK)
        for cell in self.grid:
            cell.show(self.window)
        # We update the canvas every time we draw a cell
        pygame.display.update()

    def visited_every_cell(self):
        for c in self.grid:
            if not c.visited:
                return False
        return True

    def generate(self):
        stack = []
        cell_width = WINDOW_SIZE[0] / self.w
        cell_height = WINDOW_SIZE[1] / self.h
        # initialisation of the cells
        for i in range(self.w):
            for j in range(self.h):
                self.grid.append(cell(i, j, cell_width, cell_height))
        current_cell = self.grid[CELL_ENTRANCE]
        # beginning of the creation of the maze
        while not self.visited_every_cell():
            # AFFICHER LA CONSTRUCTION !!!
            # self.show_constrution()
            next_cell = self.chose_neighbors(current_cell)
            if next_cell != -1:
                self.remove_wall(current_cell, next_cell)
                stack.append(current_cell)
                current_cell = next_cell
                current_cell.visited = True
            else:
                current_cell = stack.pop()

    def index(self, x, y):
        return int(y + x * self.w)

    def accessible_neighbors(self, c):
        neighbors = []
        index = self.index(c.x, c.y + 1)
        if 0 <= c.y + 1 < self.w and not c.walls[BOTTOM_WALL]:
            neighbors.append(self.grid[index])
        index = self.index(c.x, c.y - 1)
        if 0 <= c.y - 1 < self.w and not c.walls[TOP_WALL]:
            neighbors.append(self.grid[index])
        index = self.index(c.x + 1, c.y)
        if 0 <= c.x + 1 < self.h and not c.walls[RIGHT_WALL]:
            neighbors.append(self.grid[index])
        index = self.index(c.x - 1, c.y)
        if 0 <= c.x - 1 < self.h and not c.walls[LEFT_WALL]:
            neighbors.append(self.grid[index])
        return neighbors

    def valide_neighbors(self, c):
        neighbors = []
        index = self.index(c.x, c.y + 1)
        if 0 <= c.y + 1 < self.w and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        index = self.index(c.x, c.y - 1)
        if 0 <= c.y - 1 < self.w and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        index = self.index(c.x + 1, c.y)
        if 0 <= c.x + 1 < self.h and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        index = self.index(c.x - 1, c.y)
        if 0 <= c.x - 1 < self.h and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        return neighbors

    def chose_neighbors(self, c):
        neighbors = self.valide_neighbors(c)
        if neighbors:
            return neighbors[randint(0, len(neighbors)-1)]
        else:
            return -1

    def remove_wall(self, current, next):
        if current.x - next.x == 1:
            current.walls[LEFT_WALL] = False
            next.walls[RIGHT_WALL] = False
        if current.x - next.x == -1:
            current.walls[RIGHT_WALL] = False
            next.walls[LEFT_WALL] = False

        if current.y - next.y == 1:
            current.walls[TOP_WALL] = False
            next.walls[BOTTOM_WALL] = False

        if current.y - next.y == -1:
            current.walls[BOTTOM_WALL] = False
            next.walls[TOP_WALL] = False