'''
Our goal is to write a function that will merge two binary search trees into one doubly-linked list in sorted order.

For example:
Input: Below BSTs
 
      20
     /  \
   10    30
        /  \
       25  100
 
      50
     /  \
    5    70
 
 
Output: Below Doubly Linked List

None <- 5 <—> 10 <—> 20 <—> 25 <—> 30 <—> 50 <—> 70 <—> 100 —> null

Notice that the first element (5) in the doubly linked list is the smallest number in the two BSTs and the largest element (100) in the doubly linked list is the largest number in the two BSTs.

All of the elements in the first BST are present as well as all of the elements in the second BST, and the elements are sorted numerically.

Adapted from https://www.techiedelight.com/merge-two-bsts-into-doubly-linked-list-sorted-order/
'''


# DO NOT MODIFY THE FOLLOWING CLASSES
class BSTNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DLLNode:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def print_list(head):
        while head:
            print(head.val, end=' -> ')
            head = head.next
        print('None')

# DO NOT MODIFY THE CLASSES ABOVE

    
# Inserts a BST node at the front of a doubly linked list. You may choose to use this function in your solution or omit it if unneeded.
def push(bst_node, head):
    new_node = DLLNode(bst_node.val)
    new_node.next = head
    if head:
        head.prev = new_node
    head = new_node
    return head

# DO NOT ALTER - USED FOR TESTING
def lists_are_identical(a, b):
    while (a != None and b != None):
        if a.val != b.val:
            return False

        a = a.next
        b = b.next

    return a == None and b == None

# Recursive Helper function used to convert a BST to a doubly linked list
def convert_bst_to_ll(root, head):
    # return head if the root is empty
    if root is None:
        return head

    # we are essentially doing a reverse in-order traversal of the tree here, inserting the biggest value into the list before moving on to the second biggest value all the way until we reach the smallest value in the tree
        
    # head will store whatever is returned from running this function on the right child
    head = convert_bst_to_ll(root.right, head)
    # head will store the new head of the list, which is the new node created by pushing the value of root into the front of the list
    head = push(root, head)
    # head will store whatever is returned from running this on the left child of the tree
    head = convert_bst_to_ll(root.left, head)

    return head

# Recursive Helper function to merge two doubly linked lists
def merge_ddls(a, b):
    # base case #1: if a is empty, return b
    if a is None:
        return b

    # base case #2: if b is empty, return a
    if b is None:
        return a

    # recursive case #1: if a is less than b, set a.next to whatever is returned from a recursive call with the rest of list a and list b
    if a.val < b.val:
        a.next = merge_ddls(a.next, b)
        a.next.prev = a
        return a
    # recursive case #2: if b is less than (or equal to) a, set b.next to whatever is returned from a recursive call with list a and the rest of list b
    else:
        b.next = merge_ddls(a, b.next)
        b.next.prev = b
        return b

# Primary function, used to convert the BSTs to a linked list and then merge the resulting lists
def merge(a, b):
    first = convert_bst_to_ll(a, None)
    second = convert_bst_to_ll(b, None)
    return merge_ddls(first, second)


# Test input and assertions
'''
BST A
      20  <-- root
     /  \
   10    30
        /  \
       25  100
'''
a = BSTNode(20)
a.left = BSTNode(10)
a.right = BSTNode(30)
a.right.left = BSTNode(25)
a.right.right = BSTNode(100)

'''
BST B
      50  <-- root
     /  \
    5    70
'''
b = BSTNode(50)
b.left = BSTNode(5)
b.right = BSTNode(70)

list_1 = merge(a, b)
expected = DLLNode(5, next=DLLNode(10, next=DLLNode(20,next=DLLNode(25, next=DLLNode(30, next=DLLNode(50,next=DLLNode(70,next=DLLNode(100))))))))
assert lists_are_identical(list_1, expected)

'''
BST A
    
     22    <-- root
    /  \   
   /    \  
  5      36   
 / \    /   
3  18  25 
'''
a = BSTNode(22)
a.left = BSTNode(5)
a.right = BSTNode(36)
a.left.left = BSTNode(3)
a.left.right = BSTNode(18)
a.right.left = BSTNode(25)

'''
BST B

       85 <-- root
'''
b = BSTNode(85)

list_2 = merge(a,b)
expected = DLLNode(3, next=DLLNode(5, next=DLLNode(18,next=DLLNode(22, next=DLLNode(25, next=DLLNode(36,next=DLLNode(85)))))))
assert lists_are_identical(list_2, expected)

'''
BST A

BST B

(both empty trees)
'''

list_3 = merge(None, None)
expected = None
assert lists_are_identical(list_3, expected)

print("All tests passed! If time remains discuss time and space complexity")

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if neither of the BSTs contain any data?
A: Return None

Q: What should I do if one of the BSTs is empty?
A: Return a doubly-linked list with the data sorted from the BST with data.

Q: Will the BSTs always contain integers?
A: Yes.

Q: What do I do if the BSTs contain duplicate data?
A: You can assume there will not be duplicate data in the BSTs.

--------------------------------------------------


---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to break the problem up into parts. What are some functions we can create to divvy up the work?

 - If your candidate struggles to come up with any steps, suggest they start by writing a function that merges two sorted linked lists into one sorted linked list.

 - If your candidate struggles to convert a BST to a linked list, ask them how they may be able to turn a BST into an array (sorted or unsorted). If they can get all of the data into an array, they may be able to sort the array then write a function to turn the array into a linked list.


 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- If they used an array to help them convert a BST to a linked list, encourage them to refactor without the use of an array or additional data structure.

- If their solution did not use any recursive functions, try writing a solution that uses at least one recursive function.
"""