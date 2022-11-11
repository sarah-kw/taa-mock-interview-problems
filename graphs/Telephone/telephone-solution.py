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
    # Convert chats into a dictionary
    # Key is a person, value is a set of anhone they're in a chat with
    links = {}
    for chat in chats:
        for person in chat:
            # Make a new empty set for a person we haven't seen yet
            if person not in links:
                links[person] = set()
            # Add all the other people in that chat to their set
            for other in chat:
                if person != other:
                    links[person].add(other)

    # Initalize a visited set for our DFS
    visited = set()
    #Recursive helper for DFS
    def find_person(start, end):
        # If we've found the end person, return True
        if start == end:
            return True
        # Mark the current person as visited
        visited.add(start)
        # For all the people the current person is in chats with
        for person in links[start]:
            # Skip anyone who's already been visited
            if person in visited:
                continue
            # Recursively search
            if find_person(person, end):
                # If any one of the friends can find the person, then the current person can as well
                return True
        # If none of the friends can find the target, it's not possible
        return False

    return find_person(start, end)

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

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------


Q: What if the start and end person are the same?
A: You are guaranteed that the start and end will be two different people.

Q: What if there's only one person in a chat?
A: You are guaranteed that there will be at least two people in a chat.

Q: What should I do if there's invalid data?
A: You can assume the data will be valid.

Q: Can I mutate the input?
A: No.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, ask them what type of search algorithm would be helpful here. Either BFS or DFS can work! Have them talk through what needs to happen at each step of the search. Have them talk through an example starting with Rubens and ending with Ken.

 - Ask your candidate what way they could do to restructure the data to make it easier to work with. It's OK to guide them towards a dictionary if they're unsure how to proceed.

 - It's OK to remind your partner of the parts of the DFS/BFS they'll need - a visited set, a queue/stack, a loop/recursion. Help them talk through what should be present in each of those.

 - Encourage your candidate to print the person at each step of the search if they are not passing the test cases and are unsure why. This can help debug the path that the search takes (and can be especially helpful for debugging infinite loops).

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote a solution that used recursion, try writing a solution that uses iteration or vice versa.

- Write a function that returns how many unconnected sub-graphs are present in the data. (The number of connected collections of people)

- Write a function that finds the path that minimizes the number of people that will see the text as it's forwarded through the groups).
'''