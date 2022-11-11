'''
We are interested in writing a function to check whether a tree is a binary search tree.

For example:
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9  

Is a BST. For each node, all of the children in the left subtree are smaller, and all the children in the right subtree are larger.


However:
       5
      / \
     7   9

Is NOT a BST because 7 is greater than 5.

Write a function that takes in the root of a tree and returns a boolean indicating whether the tree is a BST.
'''


# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_BST(node):
    # Consider an empty tree as valid
    if node is None:
        return True
    # A tree with only one node is valid
    if node.left is None and node.right is None:
        return True

    # Check whether the left and right nodes are smaller
    # and greater respectively than the parent node.
    # Return False if either fails
    if ((node.left and node.left.value > node.value)
            or (node.right and node.right.value < node.value)):
        return False

    # Ensure that both subtrees are valid BSTs
    return is_BST(node.left) and is_BST(node.right)


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

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if two nodes have equal values?
A: You can assume each node will have a different value.

Q: What should I do if the input is None or has fewer than two nodes?
A: You can assume the tree will include at least one Node.

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Integers.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper.

 - If your candidate still struggles, ask them to think through the simpler case where there's only 3 nodes (the 5, 7, and 9 example in the prompt). Ask them how they would walk through that one. 

 - It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see what nodes are being visited when. This can especially help if their code gets stuck in an infinite loop.

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? Does it make a difference whether the tree is balanced or not?

- What type of traversal does the sample solution perform over the tree?

- If you wrote a recursive solution, try writing an iterative one. If you wrote an iterative solution, try writing a recursive one. Which do you prefer? What are the tradeoffs?

- Try extending your function to allow for Nodes with duplicate values.

- Try extending your function to use a custom comparator. It should accept an additional argument, `key`, that determines the order the BST ought to be using. For example, instead of checking which number is bigger, it could check which string is longer.
'''
