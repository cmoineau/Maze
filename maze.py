from cell import cell
import pygame
from variables import *
from random import randint
from time import sleep


class maze(object):
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
        sleep(0.1)

    def show(self):
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
        for i in range(self.w):
            for j in range(self.h):
                self.grid.append(cell(i, j, cell_width, cell_height))
        current_cell = self.grid[CELL_ENTRANCE]

        while not self.visited_every_cell():
            self.show_constrution()
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

    def chose_neighbors(self, c):
        neighbors = []
        x = c.x / (WINDOW_SIZE[0] / self.w)
        y = c.y / (WINDOW_SIZE[1] / self.h)
        index = self.index(x, y+1)
        if 0 <= y+1 < self.w and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        index = self.index(x, y-1)
        if 0 <= y-1 < self.w and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        index = self.index(x+1, y)
        if 0 <= x+1 < self.h and not self.grid[index].visited:
            neighbors.append(self.grid[index])
        index = self.index(x-1, y)
        if 0 <= x-1 < self.h and not self.grid[index].visited:
            neighbors.append(self.grid[index])

        if neighbors:
            return neighbors[randint(0, len(neighbors)-1)]
        else:
            return -1

    def remove_wall(self, current, next):
        n_x = next.x / (WINDOW_SIZE[0] / self.w)
        n_y = next.y / (WINDOW_SIZE[1] / self.h)
        c_x = current.x / (WINDOW_SIZE[0] / self.w)
        c_y = current.y / (WINDOW_SIZE[1] / self.h)

        if c_x - n_x == 1:
            current.walls[LEFT_WALL] = False
            next.walls[RIGHT_WALL] = False
        if c_x - n_x == -1:
            current.walls[RIGHT_WALL] = False
            next.walls[LEFT_WALL] = False

        if c_y - n_y == 1:
            current.walls[TOP_WALL] = False
            next.walls[BOTTOM_WALL] = False

        if c_y - n_y == -1:
            current.walls[BOTTOM_WALL] = False
            next.walls[TOP_WALL] = False