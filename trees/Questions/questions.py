'''
Note: The binary tree we ask you to construct below has slightly different 
properties than the binary _search_ tree we learned about in class. The order 
in which nodes are inserted into the tree is determined using a True/False 
boolean key instead of the integer keys we used in class. 

We are interested in writing an artificial intelligence that guesses what animal 
a player is thinking of by asking a series of True/False questions.

A user's answers to questions will be represented as a dictionary. For example, 
if a user was thinking of a dog, their dictionary may look like this:

{
    'gross?': False,
    'hairy?': True,
    'loyal?': True,
    'tiny?': False
}

We will store our program's questions and guesses as a binary tree. Any leaf 
node (a node with no children) will hold a guess of an animal. For example, the 
leaf node on the far left of the below tree is 'lizard'.

Each non-leaf node (any node that has at least one child) will hold a question. 
If the answer to the question is True, our program will proceed to the right 
subtree. If the answer is False, our program will proceed to the left subtree.


               hairy?
             /       \
            /         \
           /           \
       gross?          tiny?
      /    \           /    \
  lizard   beetle   loyal?  hamster
                    /   \
                 cat     dog

For example, here are a series of questions and answers (Q & A) that could lead 
to a guess:

Q: hairy?  A: True
Q: tiny?   A: False
Q: loyal?  A: True
Guess: 'dog'

Write a function that accepts a question tree and an answer dictionary, and 
returns the program's guess.
'''

# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def guesser(tree, answers):
    # Your solution here!
    tree_trace = tree
    while tree_trace.left or tree_trace.right:
        tree_trace = tree_trace.right if answers[tree_trace.value] else tree_trace.left
    return tree_trace.value



'''
               hairy?
             /       \
            /         \
           /           \
       gross?          tiny?
      /    \           /    \
  lizard   beetle   loyal?  hamster
                    /   \
                 cat     dog
'''
tree = Node("hairy?", Node("gross?", Node("lizard"), Node("beetle")), Node("tiny?", Node("loyal?", Node("cat"), Node("dog")), Node("hamster")))

answers_1 = {
    'gross?': False,
    'hairy?': True,
    'loyal?': True,
    'tiny?': False
}
assert guesser(tree, answers_1) == "dog"

# Uses same tree as above
answers_2 = {
    'gross?': False,
    'hairy?': False,
    'loyal?': False,
    'tiny?': True
}
assert guesser(tree, answers_2) == "lizard"

# Uses same tree as above
answers_3 = {
    'gross?': False,
    'hairy?': True,
    'loyal?': False,
    'tiny?': True
}
assert guesser(tree, answers_3) == "hamster"

print("All tests passed! Discuss time & space complexity if time remains")