# Name: Bread First Search
# Running Time: O(V+E)

from collections import deque

# We say a person is a seller if its name ends with a character 'm'
def person_is_seller(name):
    return name[-1] == 'm'

# The graph simulation, a person has friends
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    already_searched = [] # Persons

    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in already_searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                already_searched.append(person)
    return False

breadth_first_search("you")
