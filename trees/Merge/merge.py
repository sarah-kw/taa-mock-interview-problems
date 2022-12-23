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
 
None <-> 5 <—> 10 <—> 20 <—> 25 <—> 30 <—> 50 <—> 70 <—> 100 <—> None

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

    # You may need this to help you debug
    def print_list(head):
        while head:
            print(head.val, end=' -> ')
            head = head.next
        print('None')

# DO NOT MODIFY THE ABOVE CLASSES


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

'''
The merge function accepts two binary trees (a, b) as arguments and outputs the head (DLLNode) of a doubly linked list as a result. 

Please, alter this function for the tests below to work.
'''
def merge(a, b):
    #### FUNCTION TO BE IMPLEMENTED FOR THE MOCK INTERVIEW ####
    pass


#### Below you will find test input and assertions ####
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
# expect: 5 <-> 10 <-> 20 <-> 25 <-> 30 <-> 50 <-> 70 <-> 100
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
# expect: 3 <-> 5 <-> 18 <-> 22 <-> 25 <-> 36 <-> 85
expected = DLLNode(3, next=DLLNode(5, next=DLLNode(18,next=DLLNode(22, next=DLLNode(25, next=DLLNode(36,next=DLLNode(85)))))))
assert lists_are_identical(list_2, expected)

'''
BST A

BST B

(both empty trees)
'''
list_3 = merge(None, None)
# expect: None
expected = None
assert lists_are_identical(list_3, expected)

print("All tests passed! If time remains discuss time and space complexity")