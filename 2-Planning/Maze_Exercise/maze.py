import sys
import pygame
import random


class Node:

    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class Frontier:
    """
    Data structure that stores nodes.
    Provides functionality to select and remove nodes according to a search algorithm.
    """
    def __init__(self, goal):
        self.frontier = []
        self.goal = goal

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.select_node()
            self.frontier.remove(node)
            return node



    ####################################################################################################################
    #
    # TASK:
    # 
    # The following method selects which node from the frontier to search next. 
    # Interestingly, the selection of the next node is all you need to do to completely change the behaviour of the search algorithm.
    # Your task is to implement depth-first search, bredth first search and heuristic search.
    # as an example we've already implemented random search. 
    #
    # Tip: for heuristic search we recommend selcting the node that is closest to the goal state.
    ####################################################################################################################

    def select_node(self):
        algorithm = sys.argv[2]  # you specify this in the terminal

        # random search
        if algorithm == "RS":
            random_index = random.randrange(0,len(self.frontier))
            return self.frontier[random_index]

        # depth-first search
        if algorithm == "DFS":
            # TODO: implement depth-first search.
            return 
        
        # breadth-first search
        if algorithm == "BFS":
            # TODO: implement breadth-first search
            return
        
        # heuristic search
        if algorithm == "HS":
            # TODO: implement heuristic search
            # Note that you can access the goal state like this:
            # self.goal
            return


class Maze:
    """
    Representation of a given maze.
    Allows for implementation of different planning algorithms to find a path from start to goal.
    """
    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        # Initially, there is no solution path yet
        self.solution = None

        # Initialize an empty explored set
        self.num_explored = 0
        self.explored = set()

        # Initialize frontier with starting node
        self.starting_node = Node(state=self.start, parent=None, action=None)
        self.frontier = Frontier(goal=self.goal)
        self.frontier.add(self.starting_node)

        self.explored.add(self.starting_node)

    def neighbors(self, state):
        """
        Returns all explorable neighbouring fields of a given field in the maze.
        """
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def explore_stepwise(self):
        """Executes the next step in the path finding algorithm."""
        # If nothing left in frontier, then no path
        if self.frontier.empty():
            return

        # Choose a node from the frontier
        node = self.frontier.remove()
        self.num_explored += 1

        # If node is the goal, then we have a solution
        if node.state == self.goal:
            cells = []
            while node.parent is not None:
                cells.append(node.state)
                node = node.parent
            cells.reverse()
            self.solution = cells
            return

        # Mark node as explored
        self.explored.add(node.state)

        # Add neighbors to frontier
        for action, state in self.neighbors(node.state):
            if not self.frontier.contains_state(state) and state not in self.explored:
                child = Node(state=state, parent=node, action=action)
                self.frontier.add(child)


def main():
    if len(sys.argv) != 3:
        message = """You didn't specify the right amount of inputs.
Usage: python maze.py <maze-file-name>.txt \"<Algorithm>\"
where <Algorithm> can be DFS (Depth-first search), 
BFS (Breadth-first search), or HS (Heuristic search)."""
        sys.exit(message)

    m = Maze(sys.argv[1])

    lab_height = m.height
    lab_width = m.width

    tile_size = 40
    tile_origin = (tile_size, tile_size)

    size = width, height = (lab_width + 2) * tile_size, (lab_height + 4) * tile_size

    # Colors
    black = (0, 0, 0)
    grey = (40, 40, 40)
    white = (255, 255, 255)
    start_color = (255, 102, 102)
    goal_color = (0, 204, 0)
    explored_color = (0, 102, 102)
    frontier_color = (0, 204, 204)
    solution_color = (148, 255, 185)
    button_color = grey

    pygame.init()
    screen = pygame.display.set_mode(size)

    def draw_current_maze():
        for i in range(lab_height):
            for j in range(lab_width):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )

                pygame.draw.rect(screen, black, rect, 3)

                if m.walls[i][j]:
                    screen.fill(grey, rect)
                elif (i, j) == m.start:
                    screen.fill(start_color, rect)
                elif (i, j) == m.goal:
                    screen.fill(goal_color, rect)
                elif m.solution and (i, j) in m.solution:
                    screen.fill(solution_color, rect)
                elif (i, j) in m.explored:
                    screen.fill(explored_color, rect)
                elif any(node.state == (i, j) for node in m.frontier.frontier):
                    screen.fill(frontier_color, rect)
                else:
                    screen.fill(white, rect)

        if m.solution:
            print(f"Your algorithm explored {len(m.explored)} nodes (including start and goal).")

        pygame.display.update()

    screen.fill(black)
    draw_current_maze()
    explore_button = pygame.Rect(width/2 - 60, tile_origin[1] + (lab_height + 1) * tile_size, 120, 40)

    small_text = pygame.font.Font("freesansbold.ttf", 30)
    text_surface = small_text.render("Explore", True, white)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if explore_button.collidepoint(event.pos):
                    if not m.solution:
                        m.explore_stepwise()
                        draw_current_maze()

        pygame.draw.rect(screen, button_color, explore_button)
        screen.blit(text_surface, explore_button)
        pygame.display.update()


if __name__ == "__main__":
    main()
