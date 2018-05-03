# Name: Dijkstra
# Running Time: ?

# Graph simulation
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# Costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Proccesed nodes
proccesed_nodes = []

# Finds the node with the lowest
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    # Go through each node:
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in proccesed_nodes:
            # Set it as the new lowest cost node
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

# Find the lowest cost node that you haven't proccesed yet
node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node,
        # update the cost and its parent
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    # Mark the node as proccesed, and find the next node to process
    proccesed_nodes.append(node)
    node = find_lowest_cost_node(costs)



parent = parents["fin"]
path = ["fin"]

while parent is not None:
    path.append(parent)
    if parent not in parents:
        break
    parent = parents[parent]

print("Path and costs from the start to each node:")
print(costs)
path.reverse()
print(path)
