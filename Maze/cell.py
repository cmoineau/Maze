import pygame
from variables import *


class cell(object):
    def __init__(self, x, y, width, height):
        self.w = width
        self.h = height
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self, window):
        x = self.x * self.w
        y = self.y * self.h
        if self.walls[TOP_WALL]:
            pygame.draw.line(window, WHITE, (x, y), (x + self.w, y), LINE_SIZE)
        if self.walls[LEFT_WALL]:
            pygame.draw.line(window, WHITE, (x, y), (x, y + self.h), LINE_SIZE)
        if self.walls[RIGHT_WALL]:
            pygame.draw.line(window, WHITE, (x + self.w, y), (x + self.w, y + self.h), LINE_SIZE)
        if self.walls[BOTTOM_WALL]:
            pygame.draw.line(window, WHITE, (x, y + self.h), (x + self.w, y + self.h), LINE_SIZE)

    def show_constrution(self, window):
        x = self.x * self.w
        y = self.y * self.h

        if self.visited:
            pygame.draw.rect(window, RED, (x + 1, y + 1, self.w, self.h))
        if self.walls[TOP_WALL]:
            pygame.draw.line(window, WHITE, (x, y), (x + self.w, y), LINE_SIZE)
        if self.walls[LEFT_WALL]:
            pygame.draw.line(window, WHITE, (x, y), (x, y + self.h), LINE_SIZE)
        if self.walls[RIGHT_WALL]:
            pygame.draw.line(window, WHITE, (x + self.w, y), (x + self.w, y + self.h), LINE_SIZE)
        if self.walls[BOTTOM_WALL]:
            pygame.draw.line(window, WHITE, (x, y + self.h), (x + self.w, y + self.h), LINE_SIZE)
