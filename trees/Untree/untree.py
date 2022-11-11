'''
We are interested in converting a binary tree into a dictionary.

For example:

           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p

Would be converted to:
{
    'a': ('x', 'y'),
    'x': ('e', 'm'),
    'y': (None, 'p'),
    'e': (None, None),
    'm': (None, None),
    'p': (None, None)
}

Each key of the dictionary will be the data held by a parent node. Each value will be a tuple. The first element of the tuple will hold the data from the left child. The second element of the tuple will hold the data from the right child. If a node does not have a left and/or right child, the value in the corresponding spots in tuple will be None.

Write a function that takes in the root of a tree and returns a dictionary representation of the tree.
'''
# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def add_to_dict(dict, node):
    tup_1 = node.left.value if node.left else node.left
    tup_2 = node.right.value if node.right else node.right
    dict[node.value] = (tup_1, tup_2)

def bt_to_arr(node):
    if not node:
        return []
    return_arr = [node]
    return_arr.extend(bt_to_arr(node.left))
    return_arr.extend(bt_to_arr(node.right))
    return return_arr


def convert(tree):
    # Your solution here!
    tree_dict = dict()
    arr = bt_to_arr(tree)
    print(arr)
    for node in arr:
        add_to_dict(tree_dict, node)
    
    return tree_dict
    

'''
       d
      / \
     e   v
'''
tree = Node('d', Node('e'), Node('v'))
assert convert(tree) == {
    'd': ('e', 'v'),
    'e': (None, None),
    'v': (None, None)
}

'''
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
'''
tree = Node('a', Node('x', Node('e'), Node('m')), Node('y', None, Node('p')))
assert convert(tree) == {
    'a': ('x', 'y'),
    'x': ('e', 'm'),
    'y': (None, 'p'),
    'e': (None, None),
    'm': (None, None),
    'p': (None, None)
}


'''
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z

Valid: True
'''
tree = Node('g', Node('e', Node('k', Node('w'))), Node('f', None, Node('d', None, Node('z'))))
assert convert(tree) == {
    'g': ('e', 'f'),
    'e': ('k', None),
    'k': ('w', None),
    'w': (None, None),
    'f': (None, 'd'),
    'd': (None, 'z'),
    'z': (None, None)
}

print("All tests passed! Discuss time & space complexity if time remains.")