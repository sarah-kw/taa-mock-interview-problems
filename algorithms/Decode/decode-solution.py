'''
We are interested in determining the number of ways we can interpret a secret message provided to us as a numerical code. 

Your function will be given a string where each character is a digit.
For example:

code = "12106"

We assume that any message is encoded using the same mapping:
'A': 1
'B': 2
'C': 3
...
'Z': 26

We can see that is possible to translate the above code into 'LJF' where the code is separated into 12 (L), 10 (J), and 6 (F). Alternatively, we could translate the code into 'ABJF' where the code is separated in 1 (A), 2 (B), 10 (J), and 6 (F). Therefore, are function should return 2 as the number of ways we could interpret the given code.

Write a function that takes a code and returns the number of ways it can be decoded. 

You are guaranteed that all characters in the code will be numeric. 

Inspired by: https://leetcode.com/problems/decode-ways/
'''
    
def decode(code):

    # get the length of the code
    length = len(code)

    # if the code is an empty string, there is nothing to decode
    # if the code starts with the 0, we cannot decode it
    if length == 0 or code[0] == "0":
        return 0

    # create a memo to store the number of ways each substring can be decoded
    # memo[i] = number of ways s[0:i] can be decoded
    # the extra element (memo[0]) will be used to solve edge cases 
    memo = [0 for i in range(length + 1)]

    # initialize base cases
    # memo[0] will be used to account for edge cases such as '30' where 
    # it may seem by looking at just the first element we can decode the
    # message, but it is actually impossible
    memo[0] = 1
    memo[1] = 1

    for i in range(2, length + 1):
        
        # check if previous digit can be translated to a letter
        if 1 <= int(code[i-1:i]) <= 9:
            # add number of ways can decode s[0:i-1] to 
            # number of ways we can decode s[0:i]
            memo[i] += memo[i-1]

        # check if previous two digits can be translated to a letter
        if 10 <= int(code[i-2:i]) <= 26:
            # add number of ways can decode s[0:i-2] to
            # number of ways we can decode s[0:i]
            memo[i] += memo[i-2]

    # return the number of ways we can decode entire string
    return memo[length]
            

assert(decode('12106')) == 2
assert(decode('339')) == 1
assert(decode('306')) == 0
print("All tests passed! Discuss time & space complexity if time remains")

'''
***NOTES TO INTERVIEWER***
---------Answers to clarifying questions----------
Q: Can zeros preceding another digit be interpreted as a single digit, for example 01 as 1?
A: No. 

Q: What should I do if invalid input is passed in?
A: Assume all input is valid.

Q: What should I do if the code can't be decoded?
A: Return 0.
--------------------------------------------------

---------Hints for struggling candidates----------
- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

- Another hint is that this problem can be solved using dynamic programming. Encourage them to look for the overlapping subproblem. To solve this problem, you must consider the solution to each of the substrings, i.e., for '123', consider '1', '2', '3', '12', and '23'. Notice that the substrings overlap. 

- If your candidate struggles with the edge case where the first two digits make up a number greater than 26, give a hint that their memo can hold an extra space

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What is the time/space complexity of sample solution?

- If you solved this problem recursively, try a dynamic programming approach. If you solved this problem using dynamic programming, try a recursive approach. 
'''