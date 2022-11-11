'''
We are interested in writing a program that helps us understand dating.

We will work with a dictionary that shows us who is dating whom. In this dictionary, a person will be the key, and the value will be a *SET* containing all the people they are dating. For example:

relations = {
    "Sebastian": {"Kevin", "Lewis", "Fernando"},
    "Max": {"Fernando"},
    "Lewis": {"Sebastian"},
    "Yuki": {"Pierre"},
    "Pierre": {"Yuki"},
    "Fernando": {"Sebastian", "Max"},
    "Carlos": {"Charles", "Lando"},
    "Lando": {"Carlos"},
    "Charles": {"Carlos"},
    "Kevin": {"Sebastian"}
}

In this example, we see that Sebastian is dating 3 people: Kevin, Lewis, and Fernando. Conversely, Lewis is only dating a single person: Sebastian.

We are interested in seeing whether two people are 'connected': Whether there exists a chain of partners in between them.

For example, Lewis and Max are connected by the following chain:

- Lewis is dating Sebastian
- Sebastian is dating Fernando
- Fernando is dating Max

Therefore, Lewis and Max are connected.

On the other hand, Lewis and Yuki are NOT connected. There does not exist a chain of partners between them.

Write a function that accepts a dictionary of relationships and two different people. It should return True if the two people are connected and False if they are NOT connected.

Your function should NOT modify the dictionary nor the sets inside it.
'''

def connected(relations, person_a, person_b):
    # People we have visited so far
    visited = set()

    # Recursive helper, starting from a person trying to find a target person
    def find(start, target):
        # If we have already visited the person we don't need to search them again
        if start in visited:
            return False
        # Mark person as visited
        visited.add(start)
        # Returns True if we find the target person
        if start == target:
            return True
        # Recursively search through each of the person's partners
        for partner in relations[start]:
            found = find(partner, target)
            # If the person is found starting from any of their partners,
            # a path must exist
            if found:
                return True
        return False

    # Call the recursive helper
    return find(person_a, person_b)

# All tests use the same dictionary
relations = {
    "Sebastian": {"Kevin", "Lewis", "Fernando"},
    "Max": {"Fernando"},
    "Lewis": {"Sebastian"},
    "Yuki": {"Pierre"},
    "Pierre": {"Yuki"},
    "Fernando": {"Sebastian", "Max"},
    "Carlos": {"Charles", "Lando"},
    "Lando": {"Carlos"},
    "Charles": {"Carlos"},
    "Kevin": {"Sebastian"}
}
assert connected(relations, "Max", "Lewis") == True
assert connected(relations, "Lewis", "Yuki") == False
assert connected(relations, "Yuki", "Pierre") == True
assert connected(relations, "Lando", "Carlos") == True
assert connected(relations, "Kevin", "Carlos") == False
assert connected(relations, "Kevin", "Fernando") == True
print("All tests passed! Discuss time & space complexity if time remains.")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------


Q: Are relationships always bidirectional?
A: Yes. If person A is dating person B, you are guaranteed that person B is also dating person A. It will always go in both directions. No unrequited love here.

Q: What if I am passed a person who is not in the dictionary?
A: You are guaranteed the input person will be a key in the dictionary.

Q: Can someone show up in the values but not in the keys?
A: No. You are guaranteed that if a person shows up in the values then they will have a corresponding key in the dictionary.

Q: What if the start and end person are the same?
A: You are guaranteed that the start and end will be two different people.

Q: What should I do if there's invalid data?
A: You can assume the data will be valid.

Q: Can I mutate the input?
A: No.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, ask them what type of search algorithm would be helpful here. Either BFS or DFS can work! Have them talk through what needs to happen at each step of the search. Have them talk through an example starting with Max and ending with Lewis (reverse of the example in the prompt), and have them describe which positions would be visited in what order.

 - Encourage your candidate to print the person at each step of the search if they are not passing the test cases and are unsure why. This can help debug the path that the search takes (and can be especially helpful for debugging infinite loops).

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote a solution that used recursion, try writing a solution that uses iteration or vice versa.

- Write a function that returns the 'distance' (number of relationships) between two people in the graph. If there are multiple paths, the distance should be based on the shortest one. Note: you will need to make a more complicated graph to test on to sufficiently test this.

EXTRA HARD
- Suppose two people are trying to separate from each other. Write a function that returns the minimum number of breakups needed to make it so they are no longer connected. For example, in the below case there needs to be at least two breakups to ensure that 'x' and 'y' are no longer connected through any relationship chain. Note: you will need to make a more complicated graph to test on to sufficiently test this.

relations = {
    'x': {'b', 'c', 'd'},
    'b': {'x', 'y'},
    'c': {'x', 'y'},
    'd': {'x'},
    'y': {'b', 'c'}
}

'''
