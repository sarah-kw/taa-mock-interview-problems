'''
We are interested in determining the number of ways we can interpret a secret 
message provided to us as a numerical code. 

Your function will be given a string where each character is a digit.
For example:

code = "12106"

We assume that any message is encoded using the same mapping:
'A': 1
'B': 2
'C': 3
...
'Z': 26

We can see that is possible to translate the above code into 'LJF' where the 
code is separated into 12 (L), 10 (J), and 6 (F). Alternatively, we could 
translate the code into 'ABJF' where the code is separated in 1 (A), 2 (B), 
10 (J), and 6 (F). Therefore, are function should return 2 as the number of 
ways we could interpret the given code.

Write a function that takes a code and returns the number of ways it can be 
decoded. 

You are guaranteed that all characters in the code will be numeric. 

Inspired by: https://leetcode.com/problems/decode-ways/
'''


def decode(code):
    pass


assert (decode('12106')) == 2
assert (decode('339')) == 1
assert (decode('306')) == 0
print("All tests passed! Discuss time & space complexity if time remains")
