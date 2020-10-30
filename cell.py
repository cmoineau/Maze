import pygame
from variables import *


class cell(object):
    def __init__(self, x, y, width, height):
        self.w = width
        self.h = height
        self.x = x * width
        self.y = y * height
        self.walls = [True, False, True, True]
        self.visited = False

    def show(self, window):
        if self.walls[TOP_WALL]:
            pygame.draw.line(window, WHITE, (self.x, self.y), (self.x + self.w, self.y), LINE_SIZE)
        if self.walls[LEFT_WALL]:
            pygame.draw.line(window, WHITE, (self.x, self.y), (self.x, self.y + self.h), LINE_SIZE)
        if self.walls[RIGHT_WALL]:
            pygame.draw.line(window, WHITE, (self.x + self.w, self.y), (self.x + self.w, self.y + self.h), LINE_SIZE)
        if self.walls[BOTTOM_WALL]:
            pygame.draw.line(window, WHITE, (self.x, self.y + self.h), (self.x + self.w, self.y + self.h), LINE_SIZE)



    def show_constrution(self, window):
        if self.visited:
            pygame.draw.rect(window, RED, (self.x +1, self.y+1, self.w, self.h))
        if self.walls[TOP_WALL]:
            pygame.draw.line(window, WHITE, (self.x, self.y), (self.x + self.w, self.y), LINE_SIZE)
        if self.walls[LEFT_WALL]:
            pygame.draw.line(window, WHITE, (self.x, self.y), (self.x, self.y + self.h), LINE_SIZE)
        if self.walls[RIGHT_WALL]:
            pygame.draw.line(window, WHITE, (self.x + self.w, self.y), (self.x + self.w, self.y + self.h), LINE_SIZE)
        if self.walls[BOTTOM_WALL]:
            pygame.draw.line(window, WHITE, (self.x, self.y + self.h), (self.x + self.w, self.y + self.h), LINE_SIZE)


