'''
We are interested in finding the length of the shortest path between the top left and bottom right corner of a square matrix.

The matrix will consist of ones and zeroes. Zeroes will represent tiles that can be passed through, ones will represent impassible tiles. For example:

grid = [
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]

We will start in the top left corner can move one square at a time, left, down, up, or right. We CANNOT move diagonally. Our goal is to reach the bottom right corner in as few moves as possible

For the above grid, we can see that there is exactly one zig-zag path that takes us from the top left corner to the bottom right. We can see that it is 9 tiles long (we include the starting and ending tiles).

It is possible for there to be multiple paths. For example:

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

However, we are only interested in the length of the shortest path. In this example, the length of the shortest path is 13.

You are guaranteed that there will be at least one path that connects the top left and bottom right corner.

Write a function that takes a square grid and returns the length of the shortest path from the top left to the bottom right.
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

def path_length(grid):
    # Set to hold all the (row, column) positions that have been visited
    visited = set()
    
    # Our BFS queue will hold 2-value tuples
    # The first value will be a (row, column) position tuple
    # The second value will be the length of the path so far
    # We begin the queue at the top-left (0, 0) and a length of 1
    queue = [((0, 0), 1)]

    # Keep looping until we exhaust the queue
    while queue:
        # Dequeue the position and length
        position, length = queue.pop(0)
        # Find all next possible moves
        moves = next_moves(position, grid, visited)
        for move in moves:
            # If the move gets us to the bottom right, we've finished our path
            if move == (len(grid)-1, len(grid[0])-1):
                # We can stop immediately - a BFS visits the shortest path first
                return length + 1
            else:
                # Mark a position as visited
                visited.add(move)
                # Enqueue the postion and the current length (incremented by one to add the new position)
                queue.append((move, length+1))

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


'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if there's not a possible path? Or if the start or the end is a 1?
A: You're guaranteed that there will be at least one possible path and that the start and end will be 0.

Q: Is it possible for there to be multiple paths?
A: Yes, there can exist multiple paths from start to end. However, we are only interested in the length of the shortest one.

Q: Can your path move diagonally?
A: No, you must move either left, up, right, or down in each step.

Q: What should I do if the input is smaller than 2x2?
A: You can assume the input will have at least 4 values

Q: Is it possible to have the height and width be different? Or a ragged array?
A: No. You are guaranteed the input will be square.

Q: What should I do if invalid input is passed in?
A: Assume all input is valid.

Q: Can I mutate the input?
A: Yes.

--------------------------------------------------

---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, ask them what type of search algorithm would be helpful here. It is possible to do it with either a DFS or BFS, but a BFS is particularly well suited to this problem because it visits the shortest paths first.

 - If the candidate is still struggling, remind them about the data structures they'll need to solve this problem:
    - A set to keep track of visited nodes
    - A queue for keeping track of the nodes one needs to visit, which can also be used to store the length of the path to that node.

- Another hint is that the next moves for a position can be calculated in a separate function. Given the coordinates of a position, one can return a list of all of the next possible coordinates (up, down, left, right). Once we reach the end of the grid (len(grid) - 1, len(grid[0]) - 1), we have reached our minimum path and can immediately return the length of our current path + 1.

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? HINT: think carefully about the impact of pop(0)

- Research the deque data structure in Python. How could the sample solution be modified to use a deque? How does this impact the time complexity? https://www.geeksforgeeks.org/deque-in-python/

- The sample solution does not mutate the input. What would it look like if the input was mutated instead of using a visited set?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote a solution that used recursion, try writing a solution that uses iteration or vice versa.

- Expand your solution so that it can handle non-square matrix inputs.

- Expand your solution so it can take an arbitrary start and finish position.

EXTRA HARD
- Expand your solution so it can handle 3D input arrays. What about 4D? Or n-dimensional arrays?

EXTRA HARD
- Suppose you are allowed to change a single position from a 1 to a 0. Write a program that determines the best position to flip so that the shortest path length is minimized.
'''