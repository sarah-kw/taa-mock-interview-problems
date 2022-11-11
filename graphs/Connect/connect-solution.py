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

Write a function that takes in a square grid and returns the size of the largest 
group of zeroes.
'''


def next_moves(position, grid, visited):
    '''
    Given a (row, column) position, a grid of 1s and 0s, and a visited set
    returns a list of adjacent positions that have not been visited
    and have a value of 0
    '''

    # Holds each candidate position, changing the row or column by 1 or -1
    moves = (
        (position[0] + 1, position[1]),  # down
        (position[0] - 1, position[1]),  # up
        (position[0], position[1] + 1),  # right
        (position[0], position[1] - 1),  # left
    )

    possible = []

    # For each candidate move
    for row, column in moves:
        # Check that it's in-bounds, has a value of 0 and has not been visited
        if (0 <= row < len(grid) 
            and 0 <= column < len(grid[0])
            and grid[row][column] == 0
            and (row, column) not in visited):
            # If it satisfies all the requirements, it's a possible move
            possible.append((row, column))

    return possible


def biggest_group_size(grid):
    # Set to hold all the (row, column) positions that have been visited
    # Visited set is shared across all searches
    visited = set()

    def search(position):
        '''
        Perform a DFS starting at the given (row, column) position
        Return a count of how many non-visited connected 0s there are from 
        that start
        '''
        # Add position so we don't visit it again
        visited.add(position)
        # Start count at 1 for the position we currently occupy
        count = 1
        # Find all the places we can go next
        moves = next_moves(position, grid, visited)
        
        # Recurse through all the possible moves
        for move in moves:
            # Do not recurse through positions that have already been visited
            if move not in visited:
                # Add the amount of 0s that were found from that search
                count += search(move)
        return count

    # The size off the biggest group we've found so far
    best_size = 0

    # Iterate over every position in the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # Store the position as a tuple
            position = (row, column)
            
            # If this is a 0 and we haven't searched it before
            if position not in visited and grid[row][column] == 0:
                # Perform a search to find the size of the group
                size = search(position)
                # Update the size if bigger than the best we've seen so far
                if size > best_size:
                    best_size = size
    return best_size


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


'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------


Q: What should I do if the input is smaller than 2x2?
A: You can assume the input will have at least 4 values

Q: Is it possible to have the height and width be different? Or a ragged array?
A: No. You are guaranteed the input will be square.

Q: What should I do if invalid input is passed in? Or if there is something 
other than 1 or 0 in the matrix?
A: You can assume that the input will be valid.

Q: Can zeroes be connected diagonally?
A: Nope.

Q: Can I mutate the input?
A: Yes.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, ask them what type of 
 search algorithm would be helpful here. Either BFS or DFS can work! Have them 
 talk through what needs to happen at each step of the search. Have them talk 
 through the first example, and have them describe which positions would be 
 visited in what order.

 - If your candidate is unsure how to check every group, encourage them to 
 first solve the simpler problem of finding the size of the group that starts 
 at (0, 0). This will cause the first test to pass. If they finish that, 
 they can return to how to find any group.

 - If your candidate struggles to determine how to traverse the array, 
 encourage them first to write a helper function similar to next_moves in the 
 example. Once they have that working, they can use it in their search.

 - Encourage your candidate to print the position at each step of the search if 
 they are not passing the test cases and are unsure why. This can help debug 
 the path that the search takes (and can be especially helpful for debugging 
 infinite loops).

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution?

- The sample solution does not mutate the input. What would it look like if the 
input was mutated instead of using a visited set?

- If you wrote a solution that used DFS, try writing a solution that uses BFS 
or vice versa.

- If you wrote a solution that used recursion, try writing a solution that uses 
iteration or vice versa.

- Expand your solution so that it can handle non-square matrix inputs.

EXTRA HARD
- Expand your solution so it can handle 3D input arrays. What about 4D? Or 
n-dimensional arrays?

EXTRA HARD
- Suppose you are allowed to change a single position from a 1 to a 0. Write a 
program that determines the best position to flip so that the largest group 
size in the array is maximized.
'''