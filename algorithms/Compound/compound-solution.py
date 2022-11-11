'''
We are interested in determining whether a whether a string is made up of one or more words in a given list of vocabulary.

Your function will receive a string and a set of strings.

For example:
s = "softwareengineer"
vocab_list = {"engineer", "software", "adie")

Here we can see that the given string s is made up of two of the words in our vocab list. As a result, the function should return True. 

Note that the string can use a vocab word multiple times. 

For example:
s = "adiessupportingadies"
vocab_list = {"adies", "supporting"}

In the above example, the function should return True.

However, the string may not use the same character in multiple words. 

For example:
s = "friendsandenemies"
vocab_list = {"friends", "sand", "enemies", "end"}

The above function should return False because if we cannot share the 's' between both "friends" and "sand"

Write a function that returns True if a given string can be separated into words from a given set of vocab and False if it cannot.

'''

def segmentable(s, vocab_list):
    # get the length of the input string
    length = len(s)

    # memo[i] indicates s[:i] can be segmented into words in vocab_list
    memo = [False] * (length + 1)
    # memo[0] is an empty string so we initialize it to True
    memo[0] = True

    # Loop through s
    for i in range(1, length + 1):
        # Loop through s[0:i]
        for j in range(i):
            # if we have found that s[0:j] can be segmented 
            # and s[j:i] is also in the vocab list
            if memo[j] and s[j:i] in vocab_list:
                # we can segment s[O:i]
                memo[i] = True
                break
    # return the result for the entire string
    return memo[length]

s = "softwareengineer"
vocab_list = set(["engineer", "software", "adie"])
assert(segmentable(s, vocab_list)) == True

s = "adiessupportingadies"
vocab_list = set(["adies", "supporting"])
assert(segmentable(s, vocab_list)) == True

s = "friendsandenemies"
vocab_list = set(["friends", "sand", "enemies", "end"])
assert(segmentable(s, vocab_list)) == False

print("All tests passed! Discuss time & space complexity if time remains.")


'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if the string or vocab list is empty?
A: Assume both are non-empty. 

Q: How do I handle non alphabetic characters?
A: Assume all strings contain only alphabetic characters.

Q: What should I do if invalid input is passed in?
A: Assume all input is valid.

--------------------------------------------------

---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

- Another hint is that this problem can be solved using dynamic programming. Encourage them to look for the overlapping subproblem. To solve this problem, you must consider the solution to each of the substrings in s, many of which are overlapping.

- Another hint is that we can say that we can say an empty string can be segmented as our base case. 

 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? 

- If you wrote a brute force solution, try refactoring to use a recursive or dynamic programming approach

- If you wrote a recursive solution, try using a dynamic programming approach or vice versa.

- This problem can also be solved with a BFS or DFS traversal. How can this be considered a graph problem?

- Expand your solution so that letters can be shared amongst multiple words from the vocab list

EXTRA HARD
- Expand your solution so it constructs a sentence where each word is a valid word from the vocab list. Return all possible sentences in a list. 
For example s = "catsanddog", vocab_list = ["cat","cats","and","sand","dog"]
would return ["cats and dog","cat sand dog"]
You do not have to return each permutation of a sentence. 
For example "cats and dog" is the same as "and cats dog"

'''