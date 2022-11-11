'''
Given the head of a singly linked list, write a function is_palindrome that returns True if the list is a palindrome and False if it is not a palindrome.

For example:
5->4->2 is NOT a palindrome
5->4->5 is a palindrome

The list will be represented using the Node class below. 

You are guaranteed that the list will not have any cycles.

Adapted from: https://leetcode.com/problems/palindrome-linked-list/
'''
# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next 

def is_palindrome(head):
    vals = [] # create an empty Python list to put the values into
    current = head # current is the node we're currently looking at
    while current is not None: # while we've not reached the end of the list
        # take the curent value from the node and add it to our Python list
        vals.append(current.value)
        # move to the next node
        current = current.next
    # check whether the Python list is the same forwards and backwards
    return vals == list(reversed(vals))

    
# 5->4->2
list_1 = Node(5, Node(4, Node(2)))
assert not is_palindrome(list_1)

# 5->4->5
list_2 = Node(5, Node(4, Node(5)))
assert is_palindrome(list_2)

# a->b->c->c->b->a
list_3 = Node("a", Node("b", Node("c", Node("c", Node("b", Node("a"))))))
assert is_palindrome(list_3)

# a->b->c->E->b->a
list_4 = Node("a", Node("b", Node("c", Node("E", Node("b", Node("a"))))))
assert not is_palindrome(list_4)

# 3->3
list_5 = Node(3, Node(3))
assert is_palindrome(list_5)

# 5 (only one element in list)
list_6 = Node(5)
assert is_palindrome(list_6)

# (empty list)
list_7 = None
assert is_palindrome(list_7)
print("All tests passed! If time remains, discuss time & space complexity.")

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if the input is None?
A: Your code should treat a head of None as an empty list. We will consider an empty list to be a palindrome, so your code should return True.

Q: What should I do if the list has only a single element?
A: We will consider a single element list to be a palindrome, so your code should return True.

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Any data types that can be checked for equality.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

 - If the candidate still struggles to form an algorithm, ask them if there is a different data structure (other than a linked list) that would be easier for them to determine if it was a palindrome. Ask the candidate how they might write code that would convert the linked list into that data structure.

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGE (after interview): The given solution is O(n)/O(n) time/space complexity* where n is the number of nodes in the list. Can you come up with an O(n)/O(1) time/space complexity solution? It's a tricky one!

*assuming the size of the values are bounded by some constant
"""