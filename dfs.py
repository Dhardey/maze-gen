# DFS search
import numpy as np
from PIL import Image, ImageDraw


# Functions


def print_maze(maze):
    # Numpy method used to print out mazes in a nice way.
    print(np.matrix(maze))


def dfs(i):
    """
    This is a function for one DFS step. There are three conditions that are checked: we are at a valid height / width
    index, we are not at index 0, and the child / neighbor is not a wall. For this, a child node is defined as a
    connected empty cell, same width index but +1 height index. Note: multiple if statements are used because we may
    need to trigger / check multiple statements because I chose to implement DFS on a node instead of the whole graph.
    One step works as follows:
    1. If we are at a node with int i, look at its surrounding cells:
        a. If the node's child has no number, and it's not a wall, explore it by setting it to i+1
        b. If the node's parent has been labeled but the node's neighbor has not, explore the neighbor by setting it to i+1
        c. If the node's right neighbor has not been explored, explore it
        d. If the node's left neighbor has been explored but the child has not, explore the child.
    2. More than one of these statements can execute at once.
    """
    for a in range(0, h):
        for b in range(0, w):
            if start_matrix[a][b] == i:
                """ 
                if we are at a valid height index (a < h-1) and if the child of a node hasn't been explored,
                and it's not a wall
                """
                if a < (h - 1) and start_matrix[a + 1][b] == 0 and gen_maze[a + 1][b] == 0:
                    start_matrix[a + 1][b] = i + 1
                # if we aren't at index 0 and the parent has been explored but the neighbor has not
                if a > 0 and start_matrix[a - 1][b] > 0 and gen_maze[a][b+1] == 0:
                    start_matrix[a][b+1] = i+1
                # if we are at a valid width index and the neighboring node hasn't been visited and is not a wall
                if b < (w - 1) and start_matrix[a][b + 1] == 0 and gen_maze[a][b+1] == 0:
                    start_matrix[a][b + 1] = i + 1
                # if we aren't at index 0 and the neighbor has been explored but the child has not
                if b > 0 and start_matrix[a][b-1] > 0 and gen_maze[a+1][b] == 0:
                    start_matrix[a+1][b] = i+1


def nodes_visited():
    # This script counts how many nodes have been explored by counting how many nodes are labeled in the matrix.
    count = 0
    for a in range(0, h):
        for b in range (0, w):
            if start_matrix[a][b] > 0:
                count += 1
    return count


def shortest_dfs():
    """
    This script finds the actual solution path by:
    1. Start at the ending node and set its value to i.
    2. Add that node to the path list
    3. While i != 1:
        a. Find the next i-1 node
        b. Add that node to the path
    4. When i = 1, we are at the entrance and found the solution path
    """
    a, b = exit
    i = start_matrix[a][b]
    shortest_path = [(a, b)]
    while i > 1:
        while i > 1:
            if a > 0 and start_matrix[a - 1][b] == i - 1:
                a, b = a - 1, b
                shortest_path.append((a, b))
                i -= 1
            elif b > 0 and start_matrix[a][b - 1] == i - 1:
                a, b = a, b - 1
                shortest_path.append((a, b))
                i -= 1
            elif a < (h - 1) and start_matrix[a + 1][b] == i - 1:
                a, b = a + 1, b
                shortest_path.append((a, b))
                i -= 1
            elif b < (w - 1) and start_matrix[a][b + 1] == i - 1:
                a, b = a, b + 1
                shortest_path.append((a, b))
                i -= 1
        return shortest_path


def draw_mazes(original_maze, matrix, path):
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


# Variable inits
# For the maze I used, I will leave one uncommented out so we don't get errors throughout the script
# MAZE 1:
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
# MAZE 3

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


# Create a matrix filled with 0s. Set the entrance as the root with a 1.
start_matrix = []
for a in range(0, h):
    line = []
    for b in range(0, w):
        line.append(0)
    start_matrix.append(line)
a, b = entrance
start_matrix[a][b] = 1

"""
DFS implementation
1. Init i to 0
2. while the exit has not been explored:
    a. increment i
    b. run DFS
Note: since we increment i to 1 before running DFS, DFS will start at the root node (entrance) that's labeled 1 in above
code.
"""
i = 0
while start_matrix[exit[0]][exit[1]] == 0:
    i += 1
    dfs(i)

# Find nodes visited
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

# Find the actual path
dfs_path = shortest_dfs()

draw_mazes(gen_maze, start_matrix, dfs_path)

images = []
images[0].save("DFS_maze.jpg")

# Print the steps to the console
print_maze(start_matrix)


