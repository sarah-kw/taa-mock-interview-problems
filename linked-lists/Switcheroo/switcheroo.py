'''
We are interested in writing a function that shuffles a linked list by swapping adjacent items.

For example:
Input: a->b->c->d->e->f
Output: b->a->d->c->f->e

Notice that adjacent items have swapped position:
  a swapped with b
  c swapped with d
  e swapped with f


If there are an odd number of elements, the tail should not change position. 

For example
Input: a->b->c->d->e
Output: b->a->d->c->e

Notice that the first four elements swapped position like before, but that e remains the tail.
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
            return (type(other) == Node and self.value == other.value
                    and self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")


def shuffle(head):
    # Your solution here!
    pass


'''Tests start here'''

# Input: a->b->c->d->e->f
# Output: b->a->d->c->f->e
list_1 = Node('a', Node('b', Node('c', Node('d', Node('e', Node('f'))))))
expected = Node('b', Node('a', Node('d', Node('c', Node('f', Node('e'))))))
assert shuffle(list_1) == expected

# Input: a->b->c->d->e
# Output: b->a->d->c->e
list_2 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('b', Node('a', Node('d', Node('c', Node('e')))))
assert shuffle(list_2) == expected

# Input: 7->2
# Output: 2->7
list_3 = Node(7, Node(2))
expected = Node(2, Node(7))
assert shuffle(list_3) == expected

# Input: a
# Output: a
list_4 = Node('a')
expected = Node('a')
assert shuffle(list_4) == expected

print("All tests passed! Discuss time & space complexity if time remains.")
