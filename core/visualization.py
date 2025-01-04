import networkx as nx
import matplotlib.pyplot as plt


def visualize_steps(graph, distances, predecessors, visited):
    plt.clf()  # Clear the current figure

    # Draw the graph using networkx
    pos = nx.spring_layout(
        graph, seed=42
    )  # Layout for visualization (positions of nodes) with a fixed seed

    # Define node colors: green for visited, gray for unvisited
    node_colors = []
    for node in graph.nodes():
        if node in visited:
            node_colors.append("green")
        else:
            node_colors.append("gray")

    # Define edge colors: red for the shortest path tree, black for others
    edge_colors = []
    for edge in graph.edges():
        if predecessors.get(edge[1]) == edge[0]:
            edge_colors.append("red")
        else:
            edge_colors.append("black")

    # Draw nodes, edges, and labels
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=500,
        font_color="black",
    )

    # Add edge weights as labels
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Add distance labels (shortest path distances)
    distance_labels = {}
    for node in graph.nodes():
        if distances[node] != float("infinity"):
            distance_labels[node] = f"{distances[node]:.1f}"
        else:
            distance_labels[node] = "∞"

    # Adjust the position of the distance labels to be outside the nodes
    label_pos = {node: (pos[node][0], pos[node][1] + 0.1) for node in pos}
    nx.draw_networkx_labels(
        graph, label_pos, labels=distance_labels, font_color="purple"
    )

    # Pause to allow visualization update
    plt.pause(5)
