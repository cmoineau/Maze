# Maze

The goal of this project is to generate a maze and solve it using algorithms like A*.

## Objectives :
- Learn how to use Pygame;
- Implement a maze generator;
- Implement a path finding algorithms (A*).

## Maze generator 

In order to generate mazes, I used a backtracking algorithm ([ref.](https://en.wikipedia.org/wiki/Maze_generation_algorithm)).

The algorithm starts by creating a grid. 
Each cell has four walls (right, left, top and bottom).
The algorithm stops running when every cell has been visited.
It selects a random cell to be the current one. We then mark it has 'visited' and put this cell on a stack.
After that, it goes through the maze, by selecting the next cell from one of the neighbors of the current one which hasn't been visited yet.
It opens the wall connecting the two cells, and marks the next cell has the current one after putting it on the stack.

If the current cell has no unvisited neighbors, the current cell is set as the cell at the top of the stack.
This is the backtracking part of the algorithm.


Animation of the generation :

![maze_generation](./maze_generation.gif)
