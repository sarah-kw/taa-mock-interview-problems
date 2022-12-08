'''
We are interested in writing a function that determines if a sequence of
numbers contains two pairs (a, b) and (c, d) such that a+b = c+d. 

Your function should accept a list of integers.

For example:
numbers = [3, 10, 4, 5, 2, 14]

3 + 4 = 2 + 5. Therefore your function should return {3, 2, 4, 5} as a set. 

Note that each element of the input list will be unique. Each input will have
at most one solution. 
'''


def balanced(numbers):
    pass


assert balanced([3, 10, 4, 5, 2, 14]) == set([3, 2, 4, 5])

assert balanced([60, 0, 10, -35, 90]) == set()

assert balanced([]) == set()

print("All tests passed! Discuss time & space complexity if time remains.")