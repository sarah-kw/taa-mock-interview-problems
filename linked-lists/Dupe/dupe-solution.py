'''
Write a function that takes a *sorted* singly linked list and returns a *sorted* linked list that has the duplicates from the original removed.

For example:
Input: 3->7->7->9->9->22
Expected output: 3->7->9->22

In this example, the duplicates for 7 and 9 are removed. Note that the output is still in sorted order.

The input list will be represented using the Node class below. Your output MUST ALSO be a linked list using the provided Node class.

You are guaranteed that the list will not have any cycles.

Adapted from: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''

# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")


# IMPLEMENTATION OPTION 1: Use a seen set
def remove_duplicates(head):
    seen = {head.value} # Create a set tracking which values we've seen before
    new_head = Node(head.value) # Create a new node with the same value as the input head
    new_current = new_head
    old_current = head.next
    while old_current: # iterate through the input list
        value = old_current.value
        if value not in seen: # if we haven't seen this value before
            seen.add(value) # mark it as seen
            new_current.next = Node(value) # create a new node with the value on the tail
            new_current = new_current.next # move to the tail of our new list
        old_current = old_current.next # move to the next element of the input list
    return new_head

    
# IMPLEMENTATION OPTION 2: Modify in-place (relies on assumption that input is sorted)
def remove_duplicates(head):
    current = head # current keeps track of the node we're currently visiting
    while current is not None and current.next is not None: #iterate through each node
        if current.value == current.next.value: # if the next node is a duplicate
            current.next = current.next.next # skip it
        else: #if the next node is not a duplicate
            current = current.next # move to that node
    return head

# Input: 1->2->2->3
# Expected output: 1->2->3
list_1 = Node(1, Node(2, Node(2, Node(3))))
expected_1 = Node(1, Node(2, Node(3)))
assert remove_duplicates(list_1) == expected_1

# Input: 4->5->6
# Expected output: 4->5->6
list_2 = Node(4, Node(5, Node(6)))
expected_2 = Node(4, Node(5, Node(6)))
assert remove_duplicates(list_2) == expected_2

# Input: 3->7->7->9->9->22
# Expected output: 3->7->9->22
list_3 = Node(3, Node(7, Node(7, Node(9, Node(9, Node(22))))))
expected_3 = Node(3, Node(7, Node(9, Node(22))))
assert remove_duplicates(list_3) == expected_3

# Input: 2->5->5->5->8
# Expected output: 1->2->3
list_4 = Node(2, Node(5, Node(5, Node(5, Node(8)))))
expected_4 = Node(2, Node(5, Node(8)))
assert remove_duplicates(list_4) == expected_4

# Input: 8->8->8->8
# Expected output: 8
list_5 = Node(8, Node(8, Node(8, Node(8, Node(8)))))
expected_5 = Node(8)
assert remove_duplicates(list_5) == expected_5
print("All tests passed! If time remains, discuss time and space complexity")


"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: Should I modify the list that was passed in or create a new list?
A: You can do either.

Q: What should I do if the input is None?
A: You can assume the input will include at least two nodes and the expected output will include at least one node. 

Q: What should I do if the list has only a single element?
A: You can assume the input will include at least two nodes and the expected output will include at least one node. 

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Integers.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper.

 - If your candidate still struggles to form an algorithm, ask them what data structure might be most useful for checking if a value has been seen before.

 - It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see values are in the list that is being returned from their function.

 - It is OK for your candidate to use other intermediate data structures as part of their solution, but remind them that their final output MUST be a linked list using the provided Node class.

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):
- What are the time/space complexities of each sample solution?
- How does the __eq__ function on the Node class work? 
- What is the time/space complexity of the __eq__ function on the Node class?
- How could the __eq__ method be improved to more robustly handle cycle detection and avoid RecursionErrors?
"""