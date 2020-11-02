from maze import maze
from variables import *
from maze_solver import a_star

if __name__ == '__main__':
    a_maze_ing = maze(MAZE_SIZE)
    a_star(a_maze_ing, (0, 0), (49, 49))
    input()
