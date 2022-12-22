"""
This file will be for solving a created maze generated from the 'maze_gen.py' file. Imports: Pillow is used to create an
image of the maze and path. Numpy is used to work with matrices.
"""

from PIL import Image, ImageDraw
import numpy as np

# Functions:


def print_maze(maze):
    # Numpy method to print matrix
    print(np.matrix(maze))


def bfs(i):
    """
    This is a function for one BFS step. There are three conditions that are checked: we are at a valid height / width
    index, we are not at index 0, and the child / neighbor is not a wall. For this, a child node is defined as a
    connected empty cell, same width index but +1 height index. Note: multiple if statements are used because we may
    need to trigger / check multiple statements, so multiple statements may trigger at once since BFS is performed on a
    node.
    One step works as follows:
    1. If we are at a node with int i, look at its surrounding cells:
        a. If the node's child has no number, and it's not a wall, explore it by setting it to i+1
        b. If the node's parent has been labeled but the node's neighbor has not, explore the neighbor by setting it to i+1
        c. If the node's right neighbor has not been explored, explore it
        d. If the node's left neighbor has been explored but the child has not, explore the child.
    """
    for a in range(0, h):
        for b in range(0, w):
            if start_matrix[a][b] == i:
                # look at surrounding cell indices

                # Right neighbor
                if b < (w - 1) and start_matrix[a][b + 1] == 0 and gen_maze[a][b + 1] == 0:
                    start_matrix[a][b + 1] = i + 1
                # Left Neighbor
                if b > 0 and start_matrix[a][b - 1] == 0 and gen_maze[a][b - 1] == 0:
                    start_matrix[a][b - 1] = i + 1
                # Cell Above
                if a > 0 and start_matrix[a - 1][b] == 0 and gen_maze[a - 1][b] == 0:
                    start_matrix[a - 1][b] = i + 1
                # Child
                if a < (h - 1) and start_matrix[a + 1][b] == 0 and gen_maze[a + 1][b] == 0:
                    start_matrix[a + 1][b] = i + 1


def nodes_visited():
    """
    This function counts the number of nodes visited by scanning the matrix with a double for loop and counting how many
    nodes are > 0.
    """
    count = 0
    for a in range(0, h):
        for b in range(0, w):
            if start_matrix[a][b] != 0:
                count += 1
    return count


def shortest_bfs():
    """
    This function traces a path to the exit. It works as follows:
    1. Start at the exit, set  it to i, and add it to the path
    2. While i > 1 (since 1 is the entrance)
        a. Find the neighboring cell (up, down, left, right) that's i-1 and add it to the path
        b. Decrease i by 1
    """
    a, b = exit
    i = start_matrix[a][b]
    shortest_path = [(a, b)]
    while i > 1:
        # Top neighbor
        if a > 0 and start_matrix[a - 1][b] == i - 1:
            a, b = a - 1, b
            shortest_path.append((a, b))
            i -= 1
            # Left neighbor
        elif b > 0 and start_matrix[a][b - 1] == i - 1:
            a, b = a, b-1
            shortest_path.append((a, b))
            i -= 1
            # Bottom neighbor
        elif a < (h - 1) and start_matrix[a + 1][b] == i - 1:
            a, b = a + 1 , b
            shortest_path.append((a, b))
            i -= 1
        # Right neighbor
        elif b < (w - 1) and start_matrix[a][b + 1] == i - 1:
            a, b = a, b + 1
            shortest_path.append((a,b))
            i -= 1
    return shortest_path


def draw_maze(original_maze):
    # This script will draw out just the maze using Pillow
    image = Image.new("RGB", (zoom * w, zoom * h), white)
    just_maze = ImageDraw.Draw(image)
    for a in range(0, h):
        for b in range(0, w):
            color = white
            r = 0
            # wall
            if original_maze[a][b] == 1:
                color = black
            # entrance
            if a == entrance[0] and b == entrance[1]:
                color = dark_purple
                r = 6
            # exit
            if a == exit[0] and b == exit[1]:
                color = dark_purple
                r = 6
            just_maze.rectangle((b*zoom+r, a*zoom+r, b*zoom+zoom-r-1, a*zoom+zoom-r-1), fill=color)
    just_maze.rectangle((0, 0, zoom * w, zoom * h), outline=purple, width=2)
    images.append(image)


def draw_solution(original_maze, matrix, path):
    # Pillow module to draw an image. This will draw out the maze, the visited nodes, and the actual path
    # PIL.Image.new(mode, size, color=0)
    image = Image.new("RGB", (zoom*w, zoom*h), white)
    background = ImageDraw.Draw(image)
    for a in range(0, h):
        for b in range(0, w):
            color = white
            r = 0
            # wall
            if original_maze[a][b] == 1:
                color = black
            # entrance
            if a == entrance[0] and b == entrance[1]:
                color = dark_purple
                r = 6
            # exit
            if a == exit[0] and b == exit[1]:
                color = dark_purple
                r = 6
            background.rectangle((b*zoom+r, a*zoom+r, b*zoom+zoom-r-1, a*zoom+zoom-r-1), fill=color)
            if matrix[a][b] > 0:
                r = 6
                background.ellipse((b*zoom+r, a*zoom+r, b*zoom+zoom-r-1, a*zoom+zoom-r-1), fill=purple)

    # the path
    for c in range(len(path)-1):
        x = path[c][1]*zoom+(zoom/2)
        y = path[c][0]*zoom+(zoom/2)
        x1 = path[c+1][1]*zoom+(zoom/2)
        y1 = path[c+1][0]*zoom+(zoom/2)
        background.line((x, y, x1, y1), fill=pink, width=5)
    background.rectangle((0, 0, zoom*w, zoom*h), outline=purple, width=2)
    images.append(image)

"""
First, we need to copy over a created maze from the 'maze_gen.py' file. One of the mazes generated will be shown below.
I will use three mazes, each sized differently: small, medium, and large. 
"""


# MAZE 1
gen_maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],

    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],

    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],

    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],

    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],

    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],

    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],

]
entrance = 0, 1
exit = 9, 18
h = 10
w = 20


"""
# MAZE 2
gen_maze = [
    [1,  0,  1,  1,  1,  1,  1,  1,  1,  1],

    [1,  0,  0,  0,  0,  0,  0,  0,  0,  1],

    [1,  1,  1,  0,  1,  1,  1,  1,  1,  1],

    [1,  0,  0,  0,  0,  0,  0,  0,  0,  1],

    [1,  1,  1,  1,  1,  1,  1,  1,  0,  1],

]

#set entrance and ext
entrance = 0, 1
exit = 4, 8

# also copy over the h and w values, so we don't have to use functions like len
h = 5
w = 10
"""



"""
# MAZE 3:
gen_maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],

    [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],

    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],

]

entrance = 0, 1
exit = 4, 9
h = 5
w = 11
"""


"""
Step 1: Create a matrix filled with 0's. The entrance will be the root node and will be labeled with a '1'.
"""
start_matrix = []
for a in range(0, h):
    line = []
    for b in range(0, w):
        line.append(0)
    start_matrix.append(line)

a, b = entrance
start_matrix[a][b] = 1

"""
BFS implementation
1. Init i to 0
2. while the exit has not been explored:
    a. increment i
    b. run BFS
Note: since we increment i to 1 before running BFS, BFS will start at the root node (entrance) that's labeled 1 in above
code.
"""

i = 0
# Actually perform a BFS search until we find the exit
while start_matrix[exit[0]][exit[1]] == 0:
    i += 1
    bfs(i)
    # draw_mazes(gen_maze, start_matrix, BFS_path)

BFS_path = shortest_bfs()
nodes = nodes_visited()
print("Visited: " + str(nodes))

# Pillow Variables
# Random color palette I found
white = 255, 255, 255
black = 0, 0, 0
dark_purple = 37,27,55
purple = 55, 41, 72
pink = 255, 202, 202
light_pink = 255, 236, 239
red = 255, 0, 0
zoom = 20
borders = 6

# Array to hold Pillow Images
images = []
draw_maze(gen_maze)
images[0].save("Just_Maze.jpg")
draw_solution(gen_maze, start_matrix, BFS_path)
images[1].save("BFS_maze.jpg")





