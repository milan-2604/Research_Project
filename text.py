import matplotlib.pyplot as plt
import networkx as nx

# Create a recurrence tree using NetworkX
G = nx.DiGraph()

# Add nodes with labels representing recurrence expansion
G.add_node("T(n)\nWork: n²")
G.add_node("T(n/2)\nWork: (n/2)²")
G.add_node("T(n/2)_2\nWork: (n/2)²")
G.add_node("T(n/4)_1\nWork: (n/4)²")
G.add_node("T(n/4)_2\nWork: (n/4)²")
G.add_node("T(n/4)_3\nWork: (n/4)²")
G.add_node("T(n/4)_4\nWork: (n/4)²")

# Add edges to form the recurrence tree structure
G.add_edges_from([
    ("T(n)\nWork: n²", "T(n/2)\nWork: (n/2)²"),
    ("T(n)\nWork: n²", "T(n/2)_2\nWork: (n/2)²"),
    ("T(n/2)\nWork: (n/2)²", "T(n/4)_1\nWork: (n/4)²"),
    ("T(n/2)\nWork: (n/2)²", "T(n/4)_2\nWork: (n/4)²"),
    ("T(n/2)_2\nWork: (n/2)²", "T(n/4)_3\nWork: (n/4)²"),
    ("T(n/2)_2\nWork: (n/2)²", "T(n/4)_4\nWork: (n/4)²")
])

# Position the nodes in a hierarchical layout
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

# Draw the tree
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, arrows=False, node_size=3000, node_color='lightblue', font_size=10)
plt.title("Recurrence Tree for T(n) = 2T(n/2) + n²", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
