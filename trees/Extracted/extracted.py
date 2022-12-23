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


  


def extract(root):
    """Write your code here!"""
    pass


    

    
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
