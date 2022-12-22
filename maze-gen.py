"""
Prim's algorithm to create a maze:
1. Start with a full grid.
2. Pick a random cell, mark the cell as part of the maze and the cell's walls to a list.
3. While there are still walls in the original grid:
  a. Pick a random wall
  b. If one of the two cells the wall divides has already been visited then:
    i. Make an empty passage and add the unvisited cell as part of the maze
    ii. Add the cell's adjacent walls to the wall list.
  c. Remove the wall from the wall list.
"""

# Imports: random - for prim's algorithm; colorama - to print in a nice, viewer-friendly format
import random
from colorama import init, Fore

# for colorama
init()

# Functions


def print_maze(maze):
    """
    This function will print the maze in a nice format. There are 3 color variables:
    1. unvisited nodes, which will be BLACK
    2. empty cells, which will be MAGENTA
    3. walls, which will be CYAN
    """
    for a in range(0, h):
        for b in range(0, w):
            if maze[a][b] == 'u':
                print(Fore.BLACK + str(maze[a][b]), end=" ")
            elif maze[a][b] == ' ' or maze[a][b] == '0, ':
                print(Fore.MAGENTA + str(maze[a][b]), end=" ")
            elif maze[a][b] == '#' or maze[a][b] == '1, ':
                print(Fore.CYAN + str(maze[a][b]), end=" ")
        print('\n')


def maze_shape():
    """
    This method implements the starting shape of the maze:
    1. Populate all the arrays' indexes to undiscovered.
    2. Randomly choose entrance and make it an empty cell.
    3. Add its adjacent walls to the list and denote them as such.
    """
    for a in range(0, h):
        line = []
        for b in range(0, w):
            line.append(unvisited)
        maze.append(line)

    start_h = int(random.random() * h)
    start_w = int(random.random() * w)

    # Avoid starting on a corner
    if start_h == 0:
        start_h += 1
    if start_h == h - 1:
        start_h -= 1
    if start_w == 0:
        start_w += 1
    if start_w == w - 1:
        start_w -= 1

    # Mark adjacent cells as walls and add to wall list
    maze[start_h][start_w] = cell
    walls = []
    maze[start_h - 1][start_w] = '#'
    maze[start_h][start_w - 1] = '#'
    maze[start_h][start_w + 1] = '#'
    maze[start_h + 1][start_w] = '#'
    walls.append([start_h - 1, start_w])
    walls.append([start_h, start_w - 1])
    walls.append([start_h, start_w + 1])
    walls.append([start_h + 1, start_w])

    return walls


def check_around(r_wall):
    """
    This function checks the number of cells around the original cell. This is needed so the maze does not have a lot of
     clustered passages / hallways.
    """
    cells_around = 0
    if maze[r_wall[0] - 1][r_wall[1]] == ' ':
        cells_around += 1
    if maze[r_wall[0] + 1][r_wall[1]] == ' ':
        cells_around += 1
    if maze[r_wall[0]][r_wall[1] - 1] == ' ':
        cells_around += 1
    if maze[r_wall[0]][r_wall[1] + 1] == ' ':
        cells_around += 1
    return cells_around


def create(maze):
    """
    This function will actually create the maze using Prim's algorithm:
    1. Initialize a list to maze_shape, which will be the maze that's filled all with undiscovered-nodes.
    2. While there are walls:
        a. Pick a random undiscovered node from the wall list
        b. Pick whether wall or cell in maze
    3. Set entrance and exit to maze
    Checks:
    1. Indices: if we're on a node that's at an end index, we'll get an index error if we try to check top / left /
    right / bottom
    2. print(r_wall) after changing a node to an empty cell - just a visual check to see what indices are chosen. Right
    now it's commented out so I can see the console better.
    """
    walls = maze_shape()
    while walls:
        r_wall = walls[int(random.random() * len(walls)) - 1]
        """
        This statement prints out the random space chosen. I just used this as a visual check when righting the 
        checks below
        """
        # Need to check what wall it is
        # left
        if r_wall[1] != 0:
            """
            Checks the cells around: If the wall divides two cells and one has already been visited, make it a 
            passage. This is so we don't have random, unconnected passages.
            """
            if maze[r_wall[0]][r_wall[1] - 1] == 'u' and maze[r_wall[0]][r_wall[1] + 1] == ' ':
                # This checks how many cells are around the random pick.
                surrounding_cells = check_around(r_wall)
                # If not <2, make a cell
                if surrounding_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = ' '
                    # print(r_wall)

                    # Mark new walls, with index checks
                    # Upper
                    if r_wall[0] != 0:
                        if maze[r_wall[0] - 1][r_wall[1]] != ' ':
                            maze[r_wall[0] - 1][r_wall[1]] = '#'
                        if [r_wall[0] - 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] - 1, r_wall[1]])
                    # Lower
                    if r_wall[0] != h - 1:
                        if maze[r_wall[0] + 1][r_wall[1]] != ' ':
                            maze[r_wall[0] + 1][r_wall[1]] = '#'
                        if [r_wall[0] + 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])
                    # Left
                    if r_wall[1] != 0:
                        if maze[r_wall[0]][r_wall[1] - 1] != ' ':
                            maze[r_wall[0]][r_wall[1] - 1] = '#'
                        if [r_wall[0], r_wall[1] - 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] - 1])

                # Delete the wall from the list since it's visited
                for wall in walls:
                    if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
                        walls.remove(wall)
                continue

        # top
        if r_wall[0] != 0:
            if maze[r_wall[0] - 1][r_wall[1]] == 'u' and maze[r_wall[0] + 1][r_wall[1]] == ' ':
                surrounding_cells = check_around(r_wall)
                if surrounding_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = ' '
                    # print(r_wall)
                    if r_wall[0] != 0:
                        if maze[r_wall[0] - 1][r_wall[1]] != ' ':
                            maze[r_wall[0] - 1][r_wall[1]] = '#'
                        if [r_wall[0] - 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] - 1, r_wall[1]])
                    if r_wall[1] != 0:
                        if maze[r_wall[0]][r_wall[1] - 1] != ' ':
                            maze[r_wall[0]][r_wall[1] - 1] = '#'
                        if [r_wall[0], r_wall[1] - 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] - 1])
                    if r_wall[1] != w - 1:
                        if maze[r_wall[0]][r_wall[1] + 1] != ' ':
                            maze[r_wall[0]][r_wall[1] + 1] = '#'
                        if [r_wall[0], r_wall[1] + 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] + 1])

                for wall in walls:
                    if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
                        walls.remove(wall)
                continue

        # bottom
        if r_wall[0] != h - 1:
            if maze[r_wall[0] + 1][r_wall[1]] == 'u' and maze[r_wall[0] - 1][r_wall[1]] == ' ':
                surrounding_cells = check_around(r_wall)
                if surrounding_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = ' '
                    # print(r_wall)
                    if r_wall[0] != h - 1:
                        if maze[r_wall[0] + 1][r_wall[1]] != ' ':
                            maze[r_wall[0] + 1][r_wall[1]] = '#'
                        if [r_wall[0] + 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])
                    if r_wall[1] != 0:
                        if maze[r_wall[0]][r_wall[1] - 1] != ' ':
                            maze[r_wall[0]][r_wall[1] - 1] = '#'
                        if [r_wall[0], r_wall[1] - 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] - 1])
                    if r_wall[1] != w - 1:
                        if maze[r_wall[0]][r_wall[1] + 1] != ' ':
                            maze[r_wall[0]][r_wall[1] + 1] = '#'
                        if [r_wall[0], r_wall[1] + 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] + 1])

                for wall in walls:
                    if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
                        walls.remove(wall)
                continue

        # right
        if r_wall[1] != w-1:
            if maze[r_wall[0]][r_wall[1]+1] == "u" and maze[r_wall[0]][r_wall[1]-1] == ' ':
                surrounding_cells = check_around(r_wall)
                if surrounding_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = ' '
                    # print(r_wall)
                    if r_wall[1] != w-1:
                        if maze[r_wall[0]][r_wall[1]+1] != ' ':
                            maze[r_wall[0]][r_wall[1] + 1] = '#'
                        if [r_wall[0], r_wall[1]+1] not in walls:
                            walls.append([r_wall[0], r_wall[1] + 1])
                    if r_wall[0] != h-1:
                        if maze[r_wall[0] + 1][r_wall[1]] != ' ':
                            maze[r_wall[0] + 1][r_wall[1]] = '#'
                        if [r_wall[0] + 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])
                    if r_wall[0] != 0:
                        if maze[r_wall[0] - 1][r_wall[1]] != ' ':
                            maze[r_wall[0] - 1][r_wall[1]] = '#'
                        if [r_wall[0] - 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])
            for wall in walls:
                if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
                    walls.remove(wall)
            continue

        # Check to just delete anyway
        for wall in walls:
            if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
                walls.remove(wall)

    # Set the rest of the unvisited cells as walls in the maze
    for i in range(0, h):
        for j in range(0, w):
            if maze[i][j] == 'u':
                maze[i][j] = '#'

    """
    set enter and exit: This finds an empty cell in the row below / above the first / last row and sets the node 
    above/ below it as the entrance / exit
    """
    for a in range(0, w-1):
        if maze[1][a] == ' ':
            maze[0][a] = " "
            break

    for a in range(0, w-1):
        if maze[h - 2][a] == ' ':
            maze[h-1][a] = ' '
            break
    return maze


def convert_maze(maze):
    """
    This function is actually for later code. This just reformats the maze to be 1's and 0's.
    1's = walls
    0's = empty cells
    """
    for a in range(0, h):
        line = []
        for b in range(0, w):
            if maze[a][b] == '#':
                line.append('1, ')
            else:
                line.append('0, ')
        conv_maze.append(line)


# variable initialization
wall = '#'
cell = ' '
unvisited = 'u'
# Changeable for different size mazes
"""
Maze 1 = 10 x 20
Maze 2 = 5 x 10
Maze 3 = 5 x 11
"""
h = 5
w = 11
maze = []
conv_maze = []

maze = create(maze)
print_maze(maze)
print('\n' + '\n')
convert_maze(maze)
print('\n')
print_maze(conv_maze)

