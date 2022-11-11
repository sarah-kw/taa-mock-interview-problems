'''
We are interested in determining whether a message can be sent through a series of group chats from one person to another.

We are given a tuple of tuples representing collections of people that are in group chats together. For example:

chats = (
    ('Dwayne', 'Minh', 'Aisha'), #1
    ('Priya', 'Noor', 'Dwayne'), #2
    ('Juan', 'Jelly'), #3
    ('Allison', 'Gus'), #4
    ('Priya', 'Bethel', 'Janelle', 'Ken'), #5
    ('Noor', 'Kimi', 'Rubens'), #6
    ('Minh', 'Elora'), #7
    ('Allison', 'Gus', 'Juan'), #8
    ('Priya', 'Noor'), #9
)

For the purposes of illustration we have added comments numbering the group chats, but this is NOT a part of the data we're passed in.

In this example, we can see that Dwanye, Minh, and Aisha are in a group chat together (#1). We can also see that Priya, Noor, and Dwayne are in a separate group chat (#2). Note that a person can be a part of multiple group chats. 

If Janelle were to have a message they wanted to get to Elora, it could be forwarded through the group chats in the following way:

Janelle posts the message in the chat they're in with Priya (#5)
Priya posts the message in the chat she's in with Dwayne (#2)
Dwayne posts the message in the chat he's in with Minh (#1)
Minh posts the message in the chat they're in with Elora (#7)
(Janelle->Priya->Dwayne->Minh->Elora)

However, it is not possible for a message starting from Bethel to reach Gus. There is no sequence of forwarding that will connect the two.

Write a function that accepts a tuple of group chats, a start person, and an end person. It should return True if a message can be forwarded through a series of chats between the two people, and False if it cannot be forwarded.
'''


def can_reach(chats, start, end):
    pass


chats = (
    ('Dwayne', 'Minh', 'Aisha'),
    ('Priya', 'Noor', 'Dwayne'),
    ('Juan', 'Jelly'),
    ('Allison', 'Gus'),
    ('Priya', 'Bethel', 'Janelle', 'Ken'),
    ('Noor', 'Kimi', 'Rubens'),
    ('Minh', 'Elora'),
    ('Allison', 'Gus', 'Juan'),
    ('Priya', 'Noor'),
)
assert can_reach(chats, 'Janelle', 'Elora') == True
assert can_reach(chats, 'Bethel', 'Gus') == False
assert can_reach(chats, 'Priya', 'Noor') == True
assert can_reach(chats, 'Rubens', 'Ken') == True
assert can_reach(chats, 'Allison', 'Priya') == False
print('All tests passed! Discuss time & space complexity if time remains')
