'''
We are planning a trip and have information about what cities we'll be visiting, 
and which city will follow each one. We have this information stored in a dictionary. 
The key is the name of a city, and the value is the name of the city we plan to 
visit after that one.

For example, if we had a key:value pair of Ulaanbaatar:Irkutsk, that would mean 
we will visit Irkutsk after Ulaanbaatar.

An example of a trip itinerary is show below:

{
    "Erlian": "Ulaanbaatar",
    "Ho Chi Minh City": "Hanoi",
    "Ulaanbaatar": "Irkutsk",
    "Chengdu": "Erlian",
    "Hanoi": "Chengdu",
}

In this example, we can deduce the overall order we plan to visit cities in is as follows:
Ho Chi Minh City -> Hanoi -> Chengdu -> Erlian -> Ulaanbaatar -> Irkutsk

Note that this is NOT the order that the cities first show up in the dictionary. 
However, by looking at which city follows which, we can determine the overall order.

Write a function that takes in a trip itinerary dictionary and returns a linked 
list containing the cities in the order we plan to visit them. You must use the 
provided Node class.

You are guaranteed that the itinerary will hold exactly one sequence of cities, 
start to finish (no loops, forks, or unconnected sequences).
'''

# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

 
    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")


def convert(city_dict):
    # Your solution here!
    itinerary_start = None
    destinations = city_dict.values()
    for key in city_dict:
        if key not in destinations:
            itinerary_start = Node(key)

    city = itinerary_start
    while city.value in city_dict:
        city.next = Node(city_dict[city.value])
        city = city.next

    return itinerary_start


'''Tests start here'''

cities_1 = {
    "Nairobi": "Arusha",
    "Arusha": "Dodoma",
    "Dodoma": "Mbeya"
}
# Expected: Nairobi -> Arusha -> Dodoma -> Mbeya
expected = Node("Nairobi", Node("Arusha", Node("Dodoma", Node("Mbeya"))))
assert convert(cities_1) == expected


cities_2 = {
    "Erlian": "Ulaanbaatar",
    "Ho Chi Minh City": "Hanoi",
    "Ulaanbaatar": "Irkutsk",
    "Chengdu": "Erlian",
    "Hanoi": "Chengdu",
}
# Expected: Ho Chi Minh City -> Hanoi -> Chengdu -> Erlian -> Ulaanbaatar -> Irkutsk
expected = Node("Ho Chi Minh City", Node("Hanoi", Node("Chengdu", Node("Erlian", Node("Ulaanbaatar", Node("Irkutsk"))))))
assert convert(cities_2) == expected

cities_3 = {
    "Riga": "Klaipėda"
}
# Expected: Riga -> Klaipėda
expected = Node("Riga", Node("Klaipėda"))
assert convert(cities_3) == expected
print("All tests passed! Discuss time and space complexity if time remains")