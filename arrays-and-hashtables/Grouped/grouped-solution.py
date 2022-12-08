'''
We are interested in writing a function that take a given list of words and 
group anagrams together.


Our function should accept one argument, a list of strings. 

We will store our groups of anagrams as a set of sorted tuples. 

For example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:{
("ate, "eat", "tea"),
("nat", "tan"),
("bat",)
}

Because "eat", "tea", and "ate" are anagrams of each other, they should be 
grouped in alphabetic order as the tuple ("ate", "eat", "tea").

Similarly, the words "tan" and "nat" should be grouped together as ("nat", "tan").

Finally "bat" is not an anagram of any other word in the list, so it should 
remain by itself as ("bat",).

Note that each word in the list will be unique.
'''
from collections import defaultdict


def grouped(strings):
    # create an empty dictionary where keys will be a group of letters
    # and values will be words that are an anagram of that group of letters
    anagrams_dict = defaultdict(list)

    # loop through words in strings
    for word in strings:
        # create a list of characters making up word
        word_as_list = [char for char in word]
        # sort the list of characters
        word_as_list.sort()
        # create the key by casting the list of characters to a tuple
        key = tuple(word_as_list)

        # add the word to list of words that are an anagram of the key
        anagrams_dict[key].append(word)

    # create an empty set to store result
    answer = set()

    # loop through key-value pairs in dictionary
    for key, value in anagrams_dict.items():
        # sort the group of anagrams
        sorted_val = sorted(value)
        # cast group of anagrams to a tuple and add to set
        answer.add(tuple(sorted_val))
    # return the set
    return answer

lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
answer_1 = set([("ate", "eat", "tea"), ("bat", ), ("nat", "tan")])
assert grouped(lst) == answer_1

lst = ["bored", "players", "sadder", "dreads", "robed", "parsley"]
answer_2 = set([("bored", "robed"), ("parsley", "players"),
                ("dreads", "sadder")])
assert grouped(lst) == answer_2

lst = ["eat", "tae", "tea", "eta", "aet", "ate"]
answer_3 = set([("aet", "ate", "eat", "eta", "tae", "tea")])
assert grouped(lst) == answer_3

lst = ["eat", "ear", "tar", "pop", "pan", "pap"]
answer_4 = set([("eat", ), ("ear", ), ("tar", ), ("pop", ), ("pan", ),
                ("pap", )])
assert grouped(lst) == answer_4

lst = []
answer_5 = set()
assert grouped(lst) == answer_5

print("All tests passed! Discuss time & space complexity if time remains.")
"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: Can words in the input list contain non-alphabetic characters?
A: You can assume all words in the input list contain only alphabetic characters.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: Can a word in the input list be an empty string?
A: Yes, the input list can contain an empty string.

Q: Can a word in the input list be repeated?
A: No, you can assume all words in the input list will be unique. 

Q: Should the output be ordered in any way?
A: Yes, each tuple should be ordered alphabetically. The set of tuples does 
not need to be ordered. Since you are returning a set, the data is expected to 
be unordered and will be valid as long as the correct items are in the set. 

Q: What is an anagram?
A: Two words are anagrams of each other if the first word can be formed by 
reordering the letters of the second word and vice versa. 

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to 
 walk through an example and describe how they would do it using only pen and paper.

 - If the candidate struggles to come up with an overarching algorithm, 
 encourage them to first solve how we can determine if two words are anagrams 
 of each other.

 - If the candidate struggles with grouping anagrams together, encourage them 
 to consider what data types might lend themselves to grouping pieces of data 
 together. It may help them to know that they don't have to transform the input 
 list into a set of alphabetically sorted tuples as they find the groups of 
 anagrams. They may use some other data structure to help them sort the words 
 into their correct groups.
 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What is the time/space complexity of sample solution?

- If the candidate did not use a dictionary to implement their solution, 
encourage them to refactor their solution to use a dictionary.

"""
