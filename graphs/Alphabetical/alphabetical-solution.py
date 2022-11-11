'''
We are interested in finding the length of the longest alphabetical path of 
letters we can travel in an array.

Your function will be given a tuple of tuples of single-lowercase-letter 
strings. For example:

data = (
    ('a', 'b', 'r', 'c'),
    ('z', 'f', 'g', 'o'),
    ('i', 'h', 'q', 'x'),
    ('n', 'o', 'p', 'v')
)

Here we see that we can follow a path of adjacent letters, alphabetically. 
If we start at 'a', we could take the following path:

a->b->f->h->i->n->o->p->q->x

This path is 10 letters long. It is the longest possible path in the given data.

We consider letters to be adjacent if they are above, below, left or right of 
another letter (no diagonals). You are guaranteed that each letter in the data 
will be unique - no duplicates.

Write a function that accepts an array of letters and returns the length of the 
longest alphabetical path through the data.
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

    current_value = grid[position[0]][position[1]]

    # For each candidate move
    for row, column in moves:
        # Check that it's in-bounds, and is greater than the current value
        if (0 <= row < len(grid) 
            and 0 <= column < len(grid[0])
            and current_value < grid[row][column]):
            # If it satisfies all the requirements, it's a possible move
            possible.append((row, column))

    return possible


def longest_increasing_string(grid):
    total_best = 0

    # Recursive DFS
    def string_length(position):
        best = 0

        # Loop over each of the next possible moves
        for move in next_moves(position, grid):
            # Recurse to find the best path length starting from the neighbor
            length = string_length(move)
            # Record the best path length seen so far
            if length > best:
                best = length

        # Add 1 to include the current position in the path length
        return best + 1

    # Iterate over every starting position in the grid to find the best past length from that position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            length = string_length((i, j))
            if length > total_best:
                total_best = length

    return total_best


data = (
    ('a', 'b', 'r', 'c'),
    ('z', 'f', 'g', 'o'),
    ('i', 'h', 'q', 'x'),
    ('n', 'o', 'p', 'v')
)
# a->b->f->h->i->n->o->p->q->x
assert longest_increasing_string(data) == 10


data = (
    ('a', 'd'),
    ('b', 'c')
)
# a->b->c->d
assert longest_increasing_string(data) == 4


# Note that this data is different than the first one
data = (
    ('e', 'k', 'z', 'c'),
    ('m', 'f', 'y', 'o'),
    ('i', 'h', 'q', 'x'),
    ('n', 'o', 'p', 'v')
)
# f->h->i->n->o->p->q->y->z
assert longest_increasing_string(data) == 9

print("All tests passed! Discuss time & space complexity if time remains.")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: Can the path be connected diagonally?
A: No.

Q: What should I do if invalid input is passed in?
A: Assume all input is valid.

Q: What should I do if the starting position is outside the bounds of the grid?
A: You are guaranteed that the starting position will be in bounds of the grid.

Q: What if there are characters other than lowercase letters?
A: Assume all strings will be one letter long and will be a lowercase letter.

--------------------------------------------------

---------Hints for struggling candidates----------

- Note that the sample solution does NOT include a visited set. Because we know we can't ever 'double back' (go back to an earlier letter in the alphabet) and because we're guaranteed that there are no duplicates, we're guaranteed that the next letter we visit will not lead us into an infinite loop. In fact, a visited set can cause problems in some solutions. If your candidate is running into problems with their visited set, ask them to walk through the second, smaller test case to see if they can determine why the visited set may be a problem. If they still struggle, you can tell them a visited set is not needed for this problem.

- Another hint is that the next moves for a position can be calculated in a separate function. Given the coordinates of a position, one can return a list of all of the next possible coordinates (up, down, left, right) that have a subsequent letter in the alphabet

- Letters can be compared with < or >. letter1 < letter2 means that letter1 appears earlier in the alphabet.

- If your candidate struggles to determine where to start their search, have them first solve the simpler problem where the start of the longest path is always at (0, 0). This will allow them to pass the first two test cases. If they complete these, they can return to the larger challenge of determining an overall starting position.

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? The sample solution did not use a visited set, but is there another data structure that could have been used to prevent the same traversal down a path from being done repeatedly? If this data structure were used what would be the impact on time and space complexity?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote an iterative solution, try writing a recursive solution or vice versa.

EXTRA HARD
- Expand your solution so it can handle 3D input arrays. What about 4D? Or n-dimensional arrays?
'''