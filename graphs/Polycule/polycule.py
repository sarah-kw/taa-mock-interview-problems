'''
We are interested in writing a program that helps us understand dating.

We will work with a dictionary that shows us who is dating whom. 
In this dictionary, a person will be the key, and the value will be a *SET* 
containing all the people they are dating. For example:

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

In this example, we see that Sebastian is dating 3 people: Kevin, Lewis, and 
Fernando. Conversely, Lewis is only dating a single person: Sebastian.

We are interested in seeing whether two people are 'connected': Whether there 
exists a chain of partners in between them.

For example, Lewis and Max are connected by the following chain:

- Lewis is dating Sebastian
- Sebastian is dating Fernando
- Fernando is dating Max

Therefore, Lewis and Max are connected.

On the other hand, Lewis and Yuki are NOT connected. There does not exist a 
chain of partners between them.

Write a function that accepts a dictionary of relationships and two different 
people. It should return True if the two people are connected and False if 
they are NOT connected.

Your function should NOT modify the dictionary nor the sets inside it.
'''

def connected(relations, person_a, person_b):
    # Your solution here!
    pass

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