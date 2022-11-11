'''
We are interested in finding the length of the shortest path between the top 
left and bottom right corner of a square matrix.

The matrix will consist of ones and zeroes. Zeroes will represent tiles that 
can be passed through, ones will represent impassible tiles. For example:

grid = [
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]

We will start in the top left corner can move one square at a time, left, down, 
up, or right. We CANNOT move diagonally. Our goal is to reach the bottom right 
corner in as few moves as possible

For the above grid, we can see that there is exactly one zig-zag path that 
takes us from the top left corner to the bottom right. We can see that it is 9 
tiles long (we include the starting and ending tiles).

It is possible for there to be multiple paths. For example:

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

However, we are only interested in the length of the shortest path. In this 
example, the length of the shortest path is 13.

You are guaranteed that there will be at least one path that connects the top 
left and bottom right corner.

Write a function that takes a square grid and returns the length of the shortest 
path from the top left to the bottom right.
'''
def path_length(grid):
    pass

grid = [
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]

assert path_length(grid) == 9

grid = [
    [0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0],
]

assert path_length(grid) == 23

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

assert path_length(grid) == 13

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

assert path_length(grid) == 9

grid = [
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

assert path_length(grid) == 9

print("All tests passed! Discuss time & space complexity if time remains.")


