import heapq

# Dijkstra's Algorithm:
# 1. Set the start node's distance to 0 and all others to infinity.
# 2. Mark all nodes as unvisited.
# 3. While there are unvisited nodes:
#    a. Select the unvisited node with the smallest distance.
#    b. Update distances to its neighbors if a shorter path is found.
#    c. Mark the current node as visited.
# 4. Repeat until all nodes are visited or the shortest path is found.


def dijkstra(graph, start, target=None, visualize_step=None):
    # Initialize distances dictionary with infinity for all nodes
    distances = {}
    for node in graph:
        distances[node] = float("infinity")
    distances[start] = 0

    # Priority queue to hold nodes to explore, starting with the start node
    prioQ = [(0, start)]
    visited = set()
    predecessors = {}

    while prioQ:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(prioQ)

        # If the current distance is greater than the recorded distance, skip it
        if current_distance > distances[current_node]:
            continue

        visited.add(current_node)

        # If the target node is reached, stop the algorithm
        if target and current_node == target:
            break

        # Explore neighbors of the current node
        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]  # Ensure weight is correctly extracted
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance and add to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(prioQ, (distance, neighbor))

        # Call the visualization function if provided
        if visualize_step:
            visualize_step(graph, distances, predecessors, visited)

    return distances, predecessors
