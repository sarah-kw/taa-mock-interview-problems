'''
We are interested in writing a function to compare a given search value to a 
binary search tree. Specifically, we want to know whether the search value is 
smaller, bigger, or spanned by the tree.

Our function should accept two arguments, the root of a tree, and a search 
value to compare against it. The ouput of our functions should be as follows:

- If the value is smaller than the smallest element in the tree, our function 
should return 'smaller'
- If the value is larger than the largest element in the tree, our function 
should return 'larger'
- If the value is between the smallest and largest element (inclusive) in the 
tree, our function should return 'spanned'

For example, given this tree:

           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9

If the search value was 10, our function should return 'bigger', because 10 is 
greater than 9.
If the search value was 0, our function should return 'smaller', because 0 is 
less than 1.
If the search value was 4, our function should return 'spanned', because 4 is 
between 1 and 9 (inclusive).
If the search value was 1, our function should return 'spanned', because 1 is 
between 1 and 9 (inclusive).
'''

# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def compare_helper(tree):
    current = tree 
    smallest = 0
    largest = 0

    while current:
        if current.left:
            current = current.left
    smallest = current.val

    current = tree
    while current:
        if current.right:
            current = current.right
    largest = current.val            

    return smallest, largest
    
    
def compare(tree, search_value):
    values = compare_helper(tree)

    if search_value < values[0]:
        return "smaller"
    elif search_value > values[1]:
        return "bigger"
    else:
        return "spanned"

'''
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9
'''
tree = Node(6, Node(3, Node(1), Node(5)), Node(8, None, Node(9)))
assert compare(tree, 10) == "bigger"
assert compare(tree, 0) == "smaller"
assert compare(tree, 4) == "spanned"
assert compare(tree, 1) == "spanned"
assert compare(tree, 5) == "spanned"
assert compare(tree, 9) == "spanned"



'''
           5
         /   \
        /     \
       3       7
      /         \
     1           8
    /             
   0               
'''
tree = Node(5, Node(3, Node(1, Node(0))), Node(7, None, Node(8)))
assert compare(tree, 9) == "bigger"
assert compare(tree, -1) == "smaller"
assert compare(tree, 0) == "spanned"
assert compare(tree, 8) == "spanned"


print("All tests passed! Discuss time & space complexity if time remains")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: What should I return if the search value exactly matches the smallest value 
in the tree? What if it exactly matches the largest value?
A: You should return 'spanned'. The span is inclusive of both ends.

Q: What should I do if the input is None or has fewer than two nodes?
A: You can assume the tree will include at least two Nodes.

Q: Will the input contain any cycles?
A: No.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Integers.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to 
 walk through an example and desrcibe how they would do it using only pen and 
 paper.

 - If your candidate still struggles, ask them what the minimum value in the 
 sample tree is. Ask them how they could write code to find the minimum. Ask 
 them the same for the maximum. Ask them how the problem could be solved if 
 they knew what the minimum and maximum values of the tree are.

 - It can be challenging to debug this problem. If your candidate is failing 
 a test and unsure why, encourage them to add print statements that help them 
 see what nodes are being visited when. This can especially help if their code 
 gets stuck in an infinite loop.

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? Does it make a 
difference whether the tree is balanced or not?

- If you wrote a recursive solution, try writing an iterative one. If you 
wrote an iterative solution, try writing a recursive one. Which do you prefer? 
What are the tradeoffs?

- Try extending your function to also check whether the search value is present 
in the tree. If there's an exact match, your function should return 'present' 
instead of 'spanned'.

- Try extending your function to use a custom comparator. It should accept an 
additional argument, `key`, that determines the order the BST ought to be using. 
For example, instead of checking which number is bigger, it could check which 
string is longer.
'''