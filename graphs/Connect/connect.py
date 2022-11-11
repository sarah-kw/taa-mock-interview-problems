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

def look_for_zeros(point, grid):
    x = point[1]
    y = point[0]
    zeros = []

    if x - 1 >= 0 and grid[y][x-1] == 0:
        zeros.append((y, x-1))
    if y - 1 >= 0 and grid[y-1][x] == 0:
        zeros.append((y-1, x))
    if x + 1 < len(grid[y]) and grid[y][x+1] == 0:
        zeros.append((y, x+1))
    if y + 1 < len(grid) and grid[y+1][x] == 0:
        zeros.append((y+1, x))
    
    return zeros


def sprawl(point, grid):
    blob_size = 0
    queue = [point]
    visited = set()
    while queue:
        blob_location = queue.pop(0)
        if blob_location not in visited:
            blob_size += 1
            visited.add(blob_location)
            queue.extend(look_for_zeros(blob_location, grid))
            print(f"looked at {blob_location}")
            print(f"Blob size is {blob_size}")
    return visited, blob_size



def biggest_group_size(grid):
    biggest = 0
    group_coords = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            group_coords.append((i, j))
    
    visited = set()
    for coord in group_coords:
        if coord not in visited and grid[coord[0]][coord[1]] == 0:
            blob_visited, blob_size = sprawl(coord, grid)
            print(blob_size)
            for visited_point in blob_visited:
                visited.add(visited_point)
            if blob_size > biggest:
                biggest = blob_size

    return biggest


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