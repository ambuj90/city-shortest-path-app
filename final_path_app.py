import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, ttk, StringVar, messagebox

# Load graph from CSV
def build_graph_from_csv(file_path):
    df = pd.read_csv(file_path, header=None, names=["from", "to", "weight"])
    cities = sorted(set(df["from"]).union(set(df["to"])))
    city_index = {city: i for i, city in enumerate(cities)}
    size = len(cities)
    graph = np.zeros((size, size))
    for _, row in df.iterrows():
        i, j = city_index[row["from"]], city_index[row["to"]]
        graph[i][j] = graph[j][i] = row["weight"]
    return graph, cities

# Dijkstra’s algorithm for path
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

    # Export to file
    with open("shortest_path_result.txt", "w", encoding="utf-8") as f:
        f.write("🚀 Shortest Path Report\n")
        f.write("========================\n")
        f.write(f"From: {source}\n")
        f.write(f"To: {target}\n\n")
        f.write(f"Path: {' → '.join(path)}\n")
        f.write(f"Distance: {distance:.2f} units\n")

    return path, distance

# Visualize graph and path
def visualize_graph_with_path(graph, cities, path):
    G = nx.Graph()
    size = len(cities)
    for i in range(size):
        for j in range(i + 1, size):
            if graph[i][j] != 0:
                G.add_edge(cities[i], cities[j], weight=graph[i][j])

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)

    plt.title("City Graph with Shortest Path")
    plt.show()

# GUI Setup
def run_gui(graph, cities):
    root = Tk()
    root.title("Shortest Path Finder")
    root.geometry("400x300")

    Label(root, text="Select Starting City:").pack(pady=5)
    start_var = StringVar()
    start_menu = ttk.Combobox(root, textvariable=start_var, values=cities, state="readonly")
    start_menu.pack()

    Label(root, text="Select Destination City:").pack(pady=5)
    end_var = StringVar()
    end_menu = ttk.Combobox(root, textvariable=end_var, values=cities, state="readonly")
    end_menu.pack()

    result_label = Label(root, text="", wraplength=350, justify="center", fg="green")
    result_label.pack(pady=15)

    def on_find_path():
        source = start_var.get()
        target = end_var.get()
        if not source or not target:
            messagebox.showerror("Error", "Please select both cities.")
            return
        if source == target:
            messagebox.showinfo("Info", "Source and destination are the same.")
            return

        path, distance = find_shortest_path(graph, cities, source, target)
        result = f"🛣️ Path: {' → '.join(path)}\n📏 Distance: {distance:.2f} units"
        result_label.config(text=result)
        visualize_graph_with_path(graph, cities, path)

    Button(root, text="Find Shortest Path", command=on_find_path).pack(pady=10)

    root.mainloop()

# Main function
def main():
    file_path = "india_city_graph.csv"
    graph, cities = build_graph_from_csv(file_path)
    run_gui(graph, cities)

if __name__ == "__main__":
    main()
