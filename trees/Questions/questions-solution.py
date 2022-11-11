'''
Note: The binary tree we ask you to construct below has slightly different properties than the binary _search_ tree we learned about in class. The order in which nodes are inserted into the tree is determined using a True/False boolean key instead of the integer keys we used in class. 

We are interested in writing an artificial intelligence that guesses what animal a player is thinking of by asking a series of True/False questions.

A user's answers to questions will be represented as a dictionary. For example, if a user was thinking of a dog, their dictionary may look like this:

{
    'gross?': False,
    'hairy?': True,
    'loyal?': True,
    'tiny?': False
}

We will store our program's questions and guesses as a binary tree. Any leaf node (a node with no children) will hold a guess of an animal. For example, the leaf node on the far left of the below tree is 'lizard'.

Each non-leaf node (any node that has at least one child) will hold a question. If the answer to the question is True, our program will proceed to the right subtree. If the answer is False, our program will proceed to the left subtree.


               hairy?
             /       \
            /         \
           /           \
       gross?          tiny?
      /    \           /    \
  lizard   beetle   loyal?  hamster
                    /   \
                 cat     dog

For example, here are a series of questions and answers (Q & A) that could lead to a guess:

Q: hairy?  A: True
Q: tiny?   A: False
Q: loyal?  A: True
Guess: 'dog'

Write a function that accepts a question tree and an answer dictionary, and returns the program's guess.
'''

# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def guesser(tree, answers):
    # If the node has no children it is a leaf node and we have found the answer
    if tree.left is None and tree.right is None:
        return tree.value

    to_check = None
    # Look up the answer to the question
    if answers[tree.value]:
        # If the answer is True, we'll check the right subtree 
        to_check = tree.right
    else:
        # If the answer is False, we'll check the left subtree
        to_check = tree.left

    # Recurse to the next level of the tree
    return guesser(to_check, answers)


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

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------


Q: What should I do if the input is None or has fewer than three nodes?
A: You can assume the tree will include at least three Nodes.

Q: What should I do if there is a missing answer in the dictionary?
A: You can assume the dictionary will include the answer to every possible question.

Q: What should I do if a node has only one child?
A: You can assume each node will either be a leaf node (0 children) or have exactly 2 children.

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Strings.

Q: Do you really think cats are disloyal?
A: No, cats are amazing and I love them.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

 - If your candidate struggles to determine when to stop iteration/recursion, you can tell them that iteration/recursion should stop when a leaf node is found. Ask them how they can determine if a node is a leaf node. If they are unsure, ask them what the values of node.left and node.right will be if the node is a leaf node.

 - If your candidate struggles to debug their solution, encourage them to print the value of the node and/or the return value at each step of the iteration/recursion.

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? Does it make a difference whether the tree is balanced or not?

- If you wrote a recursive solution, try writing an iterative one. If you wrote an iterative solution, try writing a recursive one. Which do you prefer? What are the tradeoffs?

- Try extending your function to handle cases where the AI can't make a guess (a question node only has one child). Return None in this case.

- In this problem, the decision tree was provided pre-built for you. How would you go backwards, constructing a decision tree based on a collection of answer dictionaries paired with the correct animal?

SUPER EXTRA EXTREME CHALLENGE
- In this problem, it is assumed there is no ambiguity. We assume that everyone thinks that dogs are loyal and cats are not. However, that's not the case in the real world! People may have many different opinions on this and the other questions. Assume that you have many answer dictionaries, each corresponding to one person's subjective answers to a set of questions. For the sake of simplicity, let's say we're only trying to predict between whether the person is thinking of a cat or dog. Consider how would you construct a decision tree to maximize your chances of correctly guessing what the person was thinking of (knowing that it may be impossible to get 100% accuracy). Want to see how machine learning systems do this in the real world? See the below article. Warning: VERY technical. Feel free to skip over all or most of the math or parts you don't understand; you can still get a rough feel for the algorithms.
https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html
'''