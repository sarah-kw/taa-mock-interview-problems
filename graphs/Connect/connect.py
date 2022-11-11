'''
We are interested in finding the size of largest group of connected zeroes in a 
square grid.

The matrix will consist of ones and zeroes. For example:

grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

We notice that there are three groups of zeroes that are connected together. 
Zeroes are connected left, down, up, or right. They are NOT connected diagonally.

The largest of the three groups is the rectangle containing 6 zeroes in the top 
left corner. Thus, the size of the largest group is 6.

Write a function that takes in a square grid and returns the size of the 
largest group of zeroes.
'''

def biggest_group_size(grid):
    pass


grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
assert biggest_group_size(grid) == 6

grid = [
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
assert biggest_group_size(grid) == 5

grid = [
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1],
]
assert biggest_group_size(grid) == 20

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
assert biggest_group_size(grid) == 25
print("All tests passed! Discuss time & space complexity if time remains.")