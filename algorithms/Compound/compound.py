'''
We are interested in determining whether a whether a string is made up of one 
or more words in a given list of vocabulary.

Your function will receive a string and a set of strings.

For example:
s = "softwareengineer"
vocab_list = {"engineer", "software", "adie")

Here we can see that the given string s is made up of two of the words in our 
vocab list. As a result, the function should return True. 

Note that the string can use a vocab word multiple times. 

For example:
s = "adiessupportingadies"
vocab_list = {"adies", "supporting"}

In the above example, the function should return True.

However, the string may not use the same character in multiple words. 

For example:
s = "friendsandenemies"
vocab_list = {"friends", "sand", "enemies", "end"}

The above function should return False because if we cannot share the 's' 
between both "friends" and "sand"

Write a function that returns True if a given string can be separated into 
words from a given set of vocab and False if it cannot.

'''


def segmentable(s, vocab_list):
    pass


s = "softwareengineer"
vocab_list = set(["engineer", "software", "adie"])
assert (segmentable(s, vocab_list)) == True

s = "adiessupportingadies"
vocab_list = set(["adies", "supporting"])
assert (segmentable(s, vocab_list)) == True

s = "friendsandenemies"
vocab_list = set(["friends", "sand", "enemies", "end"])
assert (segmentable(s, vocab_list)) == False

print("All tests passed! Discuss time & space complexity if time remains.")
