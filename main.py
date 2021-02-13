from Maze.maze import MazeObject
from maze_solver import a_star
from variables import *

if __name__ == '__main__':
    a_maze_ing = MazeObject(MAZE_SIZE)
    entry = (0, 0)
    exit = (49, 49)
    a_star(a_maze_ing, entry, exit)
    input("Press Enter to exit !")
