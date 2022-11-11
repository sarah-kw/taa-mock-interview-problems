'''
We are interested in finding the length of the longest alphabetical path of 
letters we can travel in an array.

Your function will be given a tuple of tuples of single-lowercase-letter 
strings. For example:

data = (
    ('a', 'b', 'r', 'c'),
    ('z', 'f', 'g', 'o'),
    ('i', 'h', 'q', 'x'),
    ('n', 'o', 'p', 'v')
)

Here we see that we can follow a path of adjacent letters, alphabetically. If 
we start at 'a', we could take the following path:

a->b->f->h->i->n->o->p->q->x

This path is 10 letters long. It is the longest possible path in the given data.

We consider letters to be adjacent if they are above, below, left or right of 
another letter (no diagonals). You are guaranteed that each letter in the data 
will be unique - no duplicates.

Write a function that accepts an array of letters and returns the length of the 
longest alphabetical path through the data.
'''

def longest_increasing_string(grid):
    # Your solution here!
    pass


data = (
    ('a', 'b', 'r', 'c'),
    ('z', 'f', 'g', 'o'),
    ('i', 'h', 'q', 'x'),
    ('n', 'o', 'p', 'v')
)
# a->b->f->h->i->n->o->p->q->x
assert longest_increasing_string(data) == 10


data = (
    ('a', 'd'),
    ('b', 'c')
)
# a->b->c->d
assert longest_increasing_string(data) == 4


# Note that this data is different than the first one
data = (
    ('e', 'k', 'z', 'c'),
    ('m', 'f', 'y', 'o'),
    ('i', 'h', 'q', 'x'),
    ('n', 'o', 'p', 'v')
)
# f->h->i->n->o->p->q->y->z
assert longest_increasing_string(data) == 9

print("All tests passed! Discuss time & space complexity if time remains.")
