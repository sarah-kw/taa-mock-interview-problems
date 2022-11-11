'''
We are interested in finding the sum of a group of even numbers.

Your function will be given a 2D tuple of numbers and a starting position tuple in (row, column) format. For example:

nums = (
    (1, 2, 3, 4),
    (7, 8, 6, 4),
    (6, 9, 8, 2),
    (2, 5, 2, 1)
)
starting_position = (0, 1)

We can see that the value at starting_position is 2. We can notice that this 2 is adjacent to another even number, an 8. This 8 is adjacent to a 6, which is adjacent to other even numbers and so on. These even numbers are connected other adjacent even numbers in a group. Including the starting position, there are 8 numbers connected to it in a group. The sum of the numbers in this group is 36.

Note that the 6 and the 2 in the bottom left hand corner are NOT connected to this larger group. We only consider values that are directly above, below, left, or right of another value to be adjacent (no diagonals).

Write a function that takes a grid and a starting position and returns the sum of even numbers in a group connected to the starting position. (Include the value at the starting position in the sum).

You are guaranteed that the starting position will be in bounds of the grid and will have an even value.

'''


def next_moves(position, grid):
    '''
    Given a (row, column) positionand a grid of comparable values,
    returns a list of adjacent positions that have a value greater
    than that of the current position
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
        # Check that it's in-bounds, and is greater thsn the current value
        if (0 <= row < len(grid) 
            and 0 <= column < len(grid[0])
            and grid[row][column] % 2 == 0):
            # If it satisfies all the requirements, it's a possible move
            possible.append((row, column))

    return possible

def even_sum(grid, starting_position):
    visited = set()

    # Recursive DFS
    def group_total(position):
        visited.add(position)

        # Start total with the value at the position
        total = grid[position[0]][position[1]]
        
        # Loop over all the next possible moves
        for move in next_moves(position, grid):
            # Recursively add any unvisited sums
            if move not in visited:
                total += group_total(move)

        return total

    # Call recursive helper with the given starting position
    return group_total(starting_position)


nums = (
    (1, 2, 3, 4),
    (7, 8, 6, 4),
    (6, 9, 8, 2),
    (2, 5, 2, 1)
)
assert even_sum(nums, (0, 1)) == 36
assert even_sum(nums, (2, 2)) == 36
assert even_sum(nums, (3, 0)) == 8
print("All tests passed! Discuss time & space complexity if time remains")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: Can the group be connected diagonally?
A: No.

Q: What should I do if invalid input is passed in?
A: Assume all input is valid.

Q: What should I do if the starting position is outside the bounds of the grid or has an odd number?
A: You are guaranteed that the starting position will be in bounds of the grid and will have an even value.

--------------------------------------------------

---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, ask them what parts of the search algorithm they'll need:
    - A set to keep track of visited nodes
    - A variable to keep track of the total (if iterative) or a way         to return the total at each step (if recursive)

- Another hint is that the next moves for a position can be calculated in a separate function. Given the coordinates of a position, one can return a list of all of the next possible coordinates (up, down, left, right) that have not been visited and contain an even number

- If your candidate does not remember how to check if a number is even, you can tell them to check whether num % 2 == 0 

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote an iterative solution, try writing a recursive solution or vice versa.

EXTRA HARD
- Expand your solution so it can handle 3D input arrays. What about 4D? Or n-dimensional arrays?
'''