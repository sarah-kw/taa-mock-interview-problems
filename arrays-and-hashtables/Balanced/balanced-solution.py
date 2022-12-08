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

    # get the length of the array
    length = len(numbers)

    # create an empty dictionary to map a sum to the elements that make up that sum
    map = {}

    # loop through each element of the array
    for i in range(length):
        # loop through i+1th element to end of array
        # we exclude 0...i since we have already found the sum of i + 0...i-1
        for j in range(i+1, length):

            # find the sum of ith and jth elements 
            sum = numbers[i] + numbers[j]

            # if that sum has already been seen
            if sum in map:
                # add the elements just summed to value of map[sum]
                map[sum].append(numbers[i])
                map[sum].append(numbers[j])

                # return the answer as a set
                return set(map[sum])
            # if sum has not already been seen
            else:
                # set the sum as a new key
                # add the elements just summed as the value
                map[sum] = [numbers[i], numbers[j]]
    # if no answer has been found, return an empty set
    return set()
                

assert balanced([3, 10, 4, 5, 2, 14]) == set([3,2,4,5])

assert balanced([60, 0, 10, -35, 90]) == set()

assert balanced([]) == set()

print("All tests passed! Discuss time & space complexity if time remains.")


"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if there's an empty list?
A: See the first test case for the expected behavior. 

Q: Can the integers be negative?
A: Yes, negative integers are valid. See the third test case. 

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: Can an element be used more than once?
A: No, assume each element of the array can be used at most once in the solution.

Q: Should the output be ordered in any way?
A: No, since you are returning a set, the data is expected to be unordered and 
will be valid as long as the correct items are in the set. 
--------------------------------------------------


---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to 
 walk through an example and describe how they would do it using only pen and paper.

 - If your candidate struggles to track possible combinations of numbers, 
 encourage them to first consider the brute force solution and generate all 
 possible combinations of 4 elements of the array (this will require four 
 nested loops). 

 - If your candidate struggles to debug their solution, encourage them to print 
 the value of the numbers that they are summing at each step of the iteration. 


 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What's the complexity of the sample solution?

- If you wrote a solution without using a hash table, try refactoring your 
implementation to use a dictionary. 

- Expand you solution so that it can handle inputs containing multiple 
solutions. Your function should return a set of tuples sorted in ascending order, 
where each tuple is a solution.

For example:
Input: [2, 4, 6, 10, 0, 1]
Output: {(0,2,4,6), (0,4,6,10)}
"""