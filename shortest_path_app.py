import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load graph from CSV and build adjacency matrix
def build_graph_from_csv(file_path):
    df = pd.read_csv(file_path, header=None, names=["from", "to", "weight"])
    cities = sorted(set(df["from"]).union(set(df["to"])))
    city_index = {city: i for i, city in enumerate(cities)}

    size = len(cities)
    graph = np.zeros((size, size))

    for _, row in df.iterrows():
        i, j = city_index[row["from"]], city_index[row["to"]]
        graph[i][j] = graph[j][i] = row["weight"]  # Undirected graph

    return graph, cities

# Step 2: Find shortest path using Dijkstra
def find_shortest_path(graph, cities, source, target):
    graph_csr = csr_matrix(graph)
    src_idx = cities.index(source)
    tgt_idx = cities.index(target)

    dist_matrix, predecessors = dijkstra(csgraph=graph_csr, directed=False, indices=src_idx, return_predecessors=True)

    path = []
    i = tgt_idx
    while i != -9999:
        path.append(cities[i])
        i = predecessors[i]
    path.reverse()

    distance = dist_matrix[tgt_idx]

    # Print to console
    print(f"\n🛣️ Shortest path from {source} to {target}: {' → '.join(path)}")
    print(f"📏 Distance: {distance:.2f} units")

    # ✅ Export to file
    with open("shortest_path_result.txt", "w", encoding="utf-8") as f:
        f.write("🚀 Shortest Path Report\n")
        f.write("========================\n")
        f.write(f"From: {source}\n")
        f.write(f"To: {target}\n\n")
        f.write(f"Path: {' → '.join(path)}\n")
        f.write(f"Distance: {distance:.2f} units\n")


    print("📂 Path and distance exported to 'shortest_path_result.txt'.")

    return path


# Step 3: Visualize graph and highlight the shortest path
def visualize_graph_with_path(graph, cities, path):
    G = nx.Graph()
    size = len(cities)
    
    # Build the graph with weights
    for i in range(size):
        for j in range(i + 1, size):
            if graph[i][j] != 0:
                G.add_edge(cities[i], cities[j], weight=graph[i][j])

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Draw full graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight the shortest path in red
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)

    plt.title("City Graph with Shortest Path")
    plt.show()

# Step 4: Get valid input from user
def get_valid_city(prompt, cities):
    while True:
        city = input(prompt).strip()
        if city in cities:
            return city
        else:
            print(f"❌ '{city}' not found. Please enter a valid city from the list.")
            print(f"Available cities: {', '.join(cities)}")

# Step 5: Main CLI flow
def main():
    file_path = "india_city_graph.csv"
    graph, cities = build_graph_from_csv(file_path)

    print("\n📍 Available cities:", ", ".join(cities))

    source = get_valid_city("Enter starting city: ", cities)
    target = get_valid_city("Enter destination city: ", cities)

    path = find_shortest_path(graph, cities, source, target)

    visualize_graph_with_path(graph, cities, path)

if __name__ == "__main__":
    main()
