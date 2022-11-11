'''
We are interested in analyzing how a video gets shared with group of friends.

We will work with a dictionary that shows us who is friends with whom. In this 
dictionary, a person will be the key, and the value will be a *SET* containing 
all the people they are friends with. For example:

friend_data = {
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

In this example, we see that Sebastian has three friends: Kevin, Lewis, and 
Fernando. Conversely, Lewis only has a single friend: Sebastian.

We choose a random person to show a viral video to, and after watching it they 
share it with all their friends who share it with all their friends and so on. 
For example, if we showed Lewis our video, it would travel like this:

- Lewis watches the video
- Lewis shares the video with Sebastian
- Sebastian shares the video with Kevin and Fernando
- Fernando shares the video with Max

In this scenario, five people will end up seeing the video (Lewis, Sebastian, 
Kevin, Fernando, and Max).

Write a function that accepts a friend dictionary and an initial person to 
show it to. The function should return the overall number of people that end up
watching to movie as a result.

Your function should NOT modify the dictionary nor the sets inside it.
'''

def group_size(friend_data, start):
    # Your solution here!
    pass

friend_data = {
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

assert group_size(friend_data, "Yuki") == 2
assert group_size(friend_data, "Carlos") == 3
assert group_size(friend_data, "Charles") == 3
assert group_size(friend_data, "Lewis") == 5
assert group_size(friend_data, "Max") == 5
assert group_size(friend_data, "Sebastian") == 5
print("All tests passed. Discuss time & space complexity if time remains.")
