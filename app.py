from core.graph import DiGraph
from core.visualization import visualize_steps
from algorithms.pathfinding.dijkstra import dijkstra


def main():
    ############################################################ Dijkstra's Algorithm ############################################################

    # Create a sample graph
    graph = DiGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 2)
    graph.add_edge("A", "C", 4)
    graph.add_edge("C", "D", 1)
    graph.add_edge("B", "D", 5)

    # Run Dijkstra's algorithm
    start_node = "A"
    # target_node = "D"
    distances, _ = dijkstra(
        graph.get_graph(), start_node, visualize_step=visualize_steps
    )

    # Print detailed shortest distances
    print(f"Shortest distances from node {start_node}:")
    for node, distance in distances.items():
        if distance == float("infinity"):
            print(f"Node {node} is unreachable from node {start_node}")
        else:
            print(f"Distance to node {node}: {distance}")

    ############################################################ Placeholder ############################################################


if __name__ == "__main__":
    main()
