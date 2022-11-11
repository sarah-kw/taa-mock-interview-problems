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



def remove_duplicates(head):
    # Your solution here!
    pass


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
