from collections import defaultdict

from pyvis.network import Network
import networkx as nx


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(":") for line in f]
    return lines


def solve():
    cables = read_input()
    nx_graph = nx.Graph()
    for connections in cables:
        cable, neighbors = connections
        neighbors = neighbors.lstrip().split()
        nx_graph.add_node(cable, label=cable)
        for n in neighbors:
            nx_graph.add_node(n, label=n)
            nx_graph.add_edge(cable, n)

    edges = nx.minimum_edge_cut(nx_graph)
    for u, v in edges:
        nx_graph.remove_edge(u, v)
    sub_graphs = nx.connected_components(nx_graph)
    g1, g2 = sub_graphs
    print(len(g1) * len(g2))


solve()
