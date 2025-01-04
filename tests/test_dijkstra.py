import pytest
from algorithms.pathfinding.dijkstra import dijkstra
from core.graph import DiGraph


def test_dijkstra():
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
    distances, predecessors = dijkstra(graph.get_graph(), "A")

    # Check the shortest distances
    assert distances["A"] == 0, "Distance to start node should be 0"
    assert distances["B"] == 1, "Distance to node B should be 1"
    assert distances["C"] == 3, "Distance to node C should be 3"
    assert distances["D"] == 4, "Distance to node D should be 4"

    # Check the predecessors
    assert predecessors["B"] == "A", "Predecessor of B should be A"
    assert predecessors["C"] == "B", "Predecessor of C should be B"
    assert predecessors["D"] == "C", "Predecessor of D should be C"


if __name__ == "__main__":
    pytest.main()
