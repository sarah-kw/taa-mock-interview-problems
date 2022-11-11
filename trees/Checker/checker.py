'''
We are interested in writing a function to check whether a tree is a binary 
search tree.

For example:
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9  

Is a BST. For each node, all of the children in the left subtree are smaller, 
and all the children in the right subtree are larger.


However:
       5
      / \
     7   9

Is NOT a BST because 7 is greater than 5.

Write a function that takes in the root of a tree and returns a boolean 
indicating whether the tree is a BST.
'''


# DO NOT MODIFY THE NODE CLASS
from operator import truediv


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_BST(node):
    # Your solution here!
    if not node or (not node.left and not node.right):
        return True
    elif node.left and node.left.value > node.value:
        return False
    elif node.right and node.right.value < node.value:
        return False
    else:
        return is_BST(node.left) and is_BST(node.right)


    # return True


'''
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9

Valid: True
'''
tree = Node(6, Node(3, Node(1), Node(5)), Node(8, None, Node(9)))
assert is_BST(tree) == True

'''
       5
      / \
     7   9

Valid: False
'''
tree = Node(5, Node(7), Node(9))
assert is_BST(tree) == False

'''
       5
      / \
     3   9

Valid: False
'''
tree = Node(5, Node(3), Node(9))
assert is_BST(tree) == True

'''
       5
      / \
     3   4

Valid: False
'''
tree = Node(5, Node(3), Node(4))
assert is_BST(tree) == False

'''
           6
         /   \
        /     \
       3       8
      / \
     1   5
        /
       7

Valid: False
'''
tree = Node(6, Node(3, Node(1), Node(5, Node(7))), Node(8))
assert is_BST(tree) == False

'''
           5
         /   \
        /     \
       3       7
      /         \
     1           8
    /             \
   0               9

Valid: True
'''
tree = Node(5, Node(3, Node(1, Node(0))), Node(7, None, Node(8, None,
                                                             Node(9))))
assert is_BST(tree) == True

print("All tests passed! Discuss time & space complexity if time remains.")
