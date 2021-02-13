import pygame
from variables import *
from time import sleep


def better_cost(cell, cost, queue):
    for elts in queue:
        if elts[0] is cell and elts[1] < cost:
            return True
    return False


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def show_a_star(m, open_queue, current, end):
    m.show()
    pygame.draw.rect(m.window, RED, (current.x * current.w + 1, current.y * current.h + 1, current.w, current.h))

    pygame.draw.circle(m.window, GREEN, (end[0] * current.w + current.w/2, end[0] * current.h + current.w/2), current.w/4)

    for e in open_queue:
        c = e[0]
        pygame.draw.rect(m.window, BLUE, (c.x * c.w + 1, c.y * c.h + 1, c.w, c.h))

    pygame.display.update()
    sleep(WAIT_TIME)


def a_star(maze_to_solve, start_coor, end_coord):
    queue_open = []
    queue_close = []
    starting_cell = maze_to_solve.grid[maze_to_solve.index(start_coor[0], start_coor[1])]
    queue_open.append([starting_cell, 0, []])
    while queue_open:
        # On trie selon les heuristiques puis on sort le meilleur heuristique
        queue_open = sorted(queue_open,
               key=lambda e: e[1] + distance(e[0].x, e[0].y, end_coord[0], end_coord[1]))
        current_cell, current_cost, visited = queue_open.pop(0)

        show_a_star(maze_to_solve, queue_open, current_cell, end_coord)

        if current_cell.x == end_coord[0] and current_cell.y == end_coord[1]:
            maze_to_solve.show()
            for e in visited:
                pygame.draw.circle(maze_to_solve.window, GREEN, (e.x * e.w+ e.w/2, e.y * e.h+e.h/2), e.w/4)
            pygame.display.update()
            return 1

        for neighbor in maze_to_solve.accessible_neighbors(current_cell):
            cost = current_cost + 1
            if not (neighbor in queue_close or better_cost(neighbor, cost, queue_open)):
                queue_open.append([neighbor, cost, visited + [current_cell]])
        queue_close.append(current_cell)

    return -1
