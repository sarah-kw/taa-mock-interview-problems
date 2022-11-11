'''
We are interested in finding the fewest number of buses needed to get from one bus station to another.

We are given a dictionary where the keys are the names of stations, and the values are a list of all the numbers of the bus routes that stop at that station. For example:

stations = {
    "Central Station": [3, 22, 99],
    "Ocean Point": [18],
    "Arts District": [3, 22, 6],
    "Fairground": [18],
    "Sandpiper Elementary School": [99, 6],
    "Bobcat Middle School": [3, 7, 6],
    "Falcon High School": [7, 18]
}

We can see that buses 3, 22, and 99 stop at Central Station.

We are also given the same information in reverse: a dictionary where they keys are the bus route numbers and the values are lists of stations that the route visits:

routes = {
    3: ['Central Station', 'Arts District', 'Bobcat Middle School'],
    22: ['Central Station', 'Arts District'],
    99: ['Central Station', 'Sandpiper Elementary School'],
    18: ['Ocean Point', 'Fairground', 'Falcon High School'],
    6: ['Arts District', 'Sandpiper Elementary School', 'Bobcat Middle School'],
    7: ['Bobcat Middle School', 'Falcon High School']
}

Note that this is the same information structured in a different way. The two dictionaries are guaranteed to be consistent with one another.

We can see that to get from Ocean Point to the Arts District one possible route would be as follows:

Ocean Point -> Falcon High School (Bus 18)
Falcon High School -> Bobcat Middle School (Bus 7)
Bobcat Middle School -> Arts District (Bus 6)

This route uses three buses. There is no route between Ocean Point that uses fewer buses.

Write a function that accepts a stations dictionary, a routes dictionary, and a start and end position. It should return the minimum number of buses needed to get from the start to the end.
'''

stations = {
    "Central Station": [3, 22, 99],
    "Ocean Point": [18],
    "Arts District": [3, 22, 6],
    "Fairground": [18],
    "Sandpiper Elementary School": [99, 6],
    "Bobcat Middle School": [3, 7, 6],
    "Falcon High School": [7, 18]
}

# MAKE SURE TO UPDATE ME IF CHANGING STATIONS
routes = {
    3: ['Central Station', 'Arts District', 'Bobcat Middle School'],
    22: ['Central Station', 'Arts District'],
    99: ['Central Station', 'Sandpiper Elementary School'],
    18: ['Ocean Point', 'Fairground', 'Falcon High School'],
    6: ['Arts District', 'Sandpiper Elementary School', 'Bobcat Middle School'],
    7: ['Bobcat Middle School', 'Falcon High School']
}

def bus_count(stations, routes, start, end):
    # Initialize BFS queue
    # Will hold tuples
        # Element 0 of tuple is the location
        # Element 1 is how far away it is from the initial start
    # Begin with start location (which is 0 away from start)
    queue = [(start, 0)]
    # Start location is already visited
    visited = {start}
    while queue:
        # Dequeue and unpack
        current, length = queue.pop(0)
        # If we found the end
        if current == end:
            # Return the length from the start
            return length
        # For each of the possible bus routes to take
        for route in stations[current]:
            # For each of the stations that bus visits
            for station in routes[route]:
                # If we haven't already checked that station
                if station not in visited:
                    # Add it to visited and the back of the queue, incrementing length by one
                    visited.add(station)
                    queue.append((station, length+1))

assert bus_count(stations, routes, "Ocean Point", "Arts District") == 3
assert bus_count(stations, routes, "Falcon High School", "Fairground") == 1
assert bus_count(stations, routes, "Falcon High School", "Sandpiper Elementary School") == 2

print("All tests passed! Discuss time & space complexity if time remains.")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------


Q: Is it possible for the dictionaries to be inconsistent?
A: No, you can assume the dictionaries will be consistent with each other

Q: What should I do if there's not a possible path between the two stations?
A: You can assume that there will be a path.

Q: What if I am passed a station who is not in the dictionary?
A: You are guaranteed the start and end stations will be a keys in the stations dictionary.

Q: Can a station show up in the values but not in the keys?
A: No. You are guaranteed that if a station shows up in the values then they will have a corresponding key in the dictionary.

Q: What if the start and end station are the same?
A: You are guaranteed that the start and end will be two different stations.

Q: What should I do if there's invalid data?
A: You can assume the data will be valid.

Q: Can I mutate the input?
A: No.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, ask them what type of search algorithm would be helpful here. You can remind them that a BFS will always visit the shortest paths first. Have your candidate walk through the "Falcon High School" to "Sandpiper Elementary School" example.

 - It's OK to remind your partner of the parts of the BFS they'll need - a visited set, a queue, a loop. Help them talk through what should be present in each of those.

 - Encourage your candidate to print the station and route at each step of the search if they are not passing the test cases and are unsure why. This can help debug the path that the search takes (and can be especially helpful for debugging infinite loops).

 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? How could it be improved by using a deque?

- If you wrote a solution that used recursion, try writing a solution that uses iteration or vice versa.

- Suppose you only had the stations dictionary (not the routes one as well). How would your solution need to change?

- Suppose in addition to the above data you also have a data structure that tells you how long it takes for each bus to go from one station to another. Modify your function so that it minimizes the amount of time spent on buses instead of minimizing the number of transfers.

EXTRA HARD
- Suppose you are a city planner trying to make your city more connected by adding a single stop to an existing bus route. Write a function that determines what stop should be added to what route to minimize the average number of buses needed to transfer from one station to another.
'''
