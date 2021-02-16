from maze.maze import MazeObject
from solver import a_star
from variables import *

if __name__ == '__main__':
    entry = (0, 0)
    exit = (49, 49)
    a_maze_ing = MazeObject(MAZE_SIZE, animated=False)
    a_star.solve(a_maze_ing, entry, exit, animated=True)
    input("Press Enter to exit !")
