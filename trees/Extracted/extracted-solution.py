'''
We are interested in writing a function that creates a doubly linked list of all the leaves of a binary tree. 

Our function should accept one argument, the root of a tree. The resulting linked list should be organized such that the first element of the list is the left-most leaf in the tree, the second element of the list is the second left-most leaf in the tree, and so on. The tail of the list should be the right-most leaf.

For example, given the root of this tree:

             1
           /    \
          /      \
         2        3
       /   \    /   \
      4     5  6     7
     / \      / \    
    8   9    10 11

The function should return the following linked list: 

None <- 8 <-> 9 <-> 5 <-> 10 <-> 11 <-> 7 -> None

and return its head, 8. Note that for visual clarity, we are representing the nodes by their value 8. Our function should return the LL object itself, not just the node's value. 
'''


# DO NOT MODIFY THE CLASSES BELOW
class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class LLNode:

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DLL:

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def printDLL(self):
        '''Understanding this function is NOT necessary for solving the problem;
        it is provided to help with debugging.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next


    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        curr = self.head
        other_curr = other.head
        while curr and other_curr:
            if curr.value != other_curr.value:
                return False
    
            curr = curr.next
            other_curr = other_curr.next

        return curr is None and other_curr is None



# DO NOT MODIFY THE CLASSES ABOVE


def isLeaf(tree_node):
    # if the root ise not None
    # but its left and right children are None
    if not tree_node.left and not tree_node.right:
        # node is a leaf
        return True
    # node is not a leaf
    return False


def extract_helper(tree_node, dll):

    # base case: the tree is empty
    if not tree_node:
        # return the head of the linked list back to the main function
        return dll
    # print(tree_node.value)
    # recurse down the left subtree (this way we reach the leftmost leaf first!)
    extract_helper(tree_node.left, dll)

    # check if the current node is a leaf
    is_leaf = isLeaf(tree_node)

    # if the current node is a leaf
    if is_leaf:
        # create a new linked list node to add to the doubly linked list
        new_node = LLNode(tree_node.value)

        # if the doubly linked list is empty (this should only be true for the leftmost leaf node)
        if not dll.head:

            # set the new node as both the head and the tail of the doubly linked list
            dll.head = dll.tail = new_node

        else:
            # set the node prior to our new_node as the current tail of the doubly linked list
            new_node.prev = dll.tail
            # set the node after the current tail of the doubly linked list as the new _ode
            dll.tail.next = new_node
            # update the tail of the linked list to point at the new_node
            dll.tail = new_node
        # return early; since the node we just processed is a leaf, there is no need to recurse down its right subtree
        return

    # recurse down the right subtree
    extract_helper(tree_node.right, dll)

    # return the linked list
    return dll


def extract(root):

    # create a new doubly linked list to hold our output
    dll = DLL()

    # make an initial call to the recursive helper function
    # passing in the root of the tree and newly created linked list
    dll = extract_helper(root, dll)

    # return the head of our doubly linked list
    return dll


# test cases
'''
       3
      / \
     1   4
'''
tree = TreeNode(3, TreeNode(1), TreeNode(4))
expected = DLL(LLNode(1, next=LLNode(4)))
assert extract(tree) == expected


'''
           6
         /   \
        /     \
       4       10
      / \       \
     1   7       9
'''
tree = TreeNode(6, TreeNode(4, TreeNode(1), TreeNode(7)), TreeNode(10, None, TreeNode(9)))
expected = DLL(LLNode(1, next=LLNode(7, next=LLNode(9))))
assert extract(tree) == expected

'''
           2
         /   \
        /     \
       3       4
      /         \
     5           6
    /             \
   7               8

'''
tree = TreeNode(2, TreeNode(3, TreeNode(5, TreeNode(7))), TreeNode(4, None, TreeNode(6, None, TreeNode(8))))
expected = DLL(LLNode(7, next=LLNode(8)))
assert extract(tree) == expected

'''
    Empty Tree
'''
tree = None
expected = DLL()
assert extract(tree) == expected

print("All tests passed! If time remains discuss time and space complexity")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: Is the tree a binary search tree?
A: The tree is a binary tree but may not be a binary _search_ tree. 

Q: What should I do if the input is None?
A: You should return the head of an empty linked list (None)

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Integers.

Q: Will the tree be balanced?
A: The tree will not necessarily be balanced. 

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper. Encourage them to draw out the tree and linked list!

 - If your candidate still struggles, ask them how they would like to traverse the tree using pen and paper. Does the order in which they process the nodes matter (think about looking at the left child, right child, and current root)?

 - If your candidate still struggles, suggest that they first try and find all the leaves in the tree. Instead of adding the leaves to a doubly linked list, add the leaves' values to an array. If they are able to solve that subproblem, they can attempt to extend their code to instead add the leaf nodes to a linked list. 

 - It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see what nodes are being visited when. This can especially help if their code gets stuck in an infinite loop.


 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? Does it make a difference whether the tree is balanced or not?

- If you wrote a recursive solution, try writing an iterative one. If you wrote an iterative solution, try writing a recursive one. Which do you prefer? What are the tradeoffs?

- Try extending your function to also remove all of the leaves from the binary search tree. 

- Try refactoring your solution so that it uses the Tree class to represent the doubly linked list instead of the LinkedList class. How can we represent a doubly linked list using our Tree class?
'''
