'''
We are interested in converting a binary tree into a dictionary.

For example:

           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p

Would be converted to:
{
    'a': ('x', 'y'),
    'x': ('e', 'm'),
    'y': (None, 'p'),
    'e': (None, None),
    'm': (None, None),
    'p': (None, None)
}

Each key of the dictionary will be the data held by a parent node. Each value 
will be a tuple. The first element of the tuple will hold the data from the 
left child. The second element of the tuple will hold the data from the right 
child. If a node does not have a left and/or right child, the value in the 
corresponding spots in tuple will be None.

Write a function that takes in the root of a tree and returns a dictionary 
representation of the tree.
'''
# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def convert(tree):
    # Initalize empty dictionary that will be mutated to hold
    # the results
    result = {}
    # Traverse tree, mutating the result dictionary
    traverse_and_fill(tree, result)
    return result

def traverse_and_fill(node, to_fill):
    ''' 
    Helper function to recursively traverses the tree, adding keys/values
    to to_fill dictionary. Keys are the data the parent nodes hold,
    values are a tuple with the data the left and right children hold.
    '''
    
    # No need to alter the dictionary if the tree is empty
    if node is None:
        return

    # Default the data from the left and right nodes to None
    left_val, right_val = None, None

    # Only replace the data for each if each child is not None
    if node.left:
        left_val = node.left.value
    if node.right:
        right_val = node.right.value

    # Mutate the dictionary
    # Parent data is key
    # Child data is put into tuples
    to_fill[node.value] = (left_val, right_val)

    # Recurse down each subtree
    traverse_and_fill(node.left, to_fill)
    traverse_and_fill(node.right, to_fill)


'''
       d
      / \
     e   v
'''
tree = Node('d', Node('e'), Node('v'))
assert convert(tree) == {
    'd': ('e', 'v'),
    'e': (None, None),
    'v': (None, None)
}

'''
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
'''
tree = Node('a', Node('x', Node('e'), Node('m')), Node('y', None, Node('p')))
assert convert(tree) == {
    'a': ('x', 'y'),
    'x': ('e', 'm'),
    'y': (None, 'p'),
    'e': (None, None),
    'm': (None, None),
    'p': (None, None)
}


'''
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z

Valid: True
'''
tree = Node('g', Node('e', Node('k', Node('w'))), Node('f', None, Node('d', None, Node('z'))))
assert convert(tree) == {
    'g': ('e', 'f'),
    'e': ('k', None),
    'k': ('w', None),
    'w': (None, None),
    'f': (None, 'd'),
    'd': (None, 'z'),
    'z': (None, None)
}

print("All tests passed! Discuss time & space complexity if time remains.")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------


Q: What should I do if the input is None or has fewer than three nodes?
A: You can assume the tree will include at least three Nodes.

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Strings.

Q: What should I do if there are duplicate values in the tree?
A: You can assume every value in the tree will be unique.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk 
 through an example and describe how they would do it using only pen and paper.

 - If your candidate struggles to determine how to do the iteration / recursion, 
 encourage them to first do the simpler case where there is only one parent with 
 two children (the first test case). If they complete that case, they can 
 revisit the logic to traverse the tree.

 - Encourage your candidate to print the result if they are not passing the 
 test cases and are unsure why. If their dictionary contains the actual node 
 objects, remind them that we want the dictionary to hold the data stored in 
 the nodes, not the nodes themselves.

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? Does it make a 
difference whether the tree is balanced or not?

- What are the tradeoffs between storing this data using nodes vs using a 
dictionary? Which do you prefer in what cases?

- If you wrote a recursive solution, try writing an iterative one. If you wrote 
an iterative solution, try writing a recursive one. Which do you prefer? 
What are the tradeoffs?

- Modify the Node class so that each node can have any number of children. 
Modify your solution to handle representing these new trees.

EXTRA HARD
- Can you think of how to represent a binary tree using only a single 
dimensional list? Make it so finding the root is O(1) and finding the children 
of a given node is also O(1). What are the tradeoffs of storing a binary tree 
in this format?
'''