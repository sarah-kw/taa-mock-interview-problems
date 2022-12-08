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


def grouped(s):
    pass


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