## Task Overview:

This is a simple exercise that lets you visualize the difference between search strategies in a labyrinth search scenario. It is designed to:

1. Illustrate how breadth-first search, depth-first search and heuristic search differ in their search behaviour
2. show you how small the algorithmic changes between the three search algorithms really are.
   You will implement all three algorithms just by changing how the search algorithms selects the next node to visit.

## Detailed Description:

In the attached zip file, you will find a python program "maze.py" and five different mazes (.txt). The python program can load a maze and apply a search algorithm to find a way through it. The search process is illustrated as in the attached image. The program illustrates:

1. Start: the position the search originates from
2. Goal: the position that is searched
3. Explored: all positions that have already been searched
4. Frontier: all positions that could be searched next.

## How to execute the program:

The program expects two input parameters. The first one is the file that contains the maze. The second one is the search algorithm to use. The file can be any file that is in the same folder. For example, "maze1.txt". The search algorithm ca be "RS" for random search, "BFS" for breadth-first search, "DFS" for depth-first search and "HS" for heuristic search.
For example, if you want to execute maze 3 with heuristic search you execute the following line:

- python maze3.txt HS
  Once you have started the program you can click on “Explore” to execute one step in the search process.

## Your task is twofold:

In the first part you write a function select node (see TODOs in maze.py). This function selects which node from the frontier to search next. You will implement three variations of this function: breadth-first search, depth-first search, and heuristic search. All of this can be achieved by just selecting an appropriate node from the frontier. No other changes are necessary. We implemented random search already as an example.

In the second part please execute all mazes and count how long each search algorithm takes. After the algorithm has found a goal it will print the number of steps it took into the command line. No need to count your clicks.

## Tips:

- This classroom contains pseudo code for all three search algorithms. You won't need to implement it completely, but it can be a good starting point to understand which node from the frontier to select
- For heuristic search we recommend selecting the node closest to the goal node.
