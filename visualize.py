import networkx as nx
import matplotlib.pyplot as plt  
import csv

nodeFile = "Nodes_NO_NM_WKG_3.csv"
edgeFile = "Edges_NO_NM_WKG_3.csv"
nodes = {}
edges = {}

with open(nodeFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nodes[row['id']] = row

with open(edgeFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        edges[row['S'] + row['T']] = row

graph = nx.Graph()
for nd in nodes:
    graph.add_node(nd, **nodes[nd])
for ed in edges:
    graph.add_edge(edges[ed]["S"], edges[ed]["T"], **edges[ed])

nx.draw_networkx(graph, with_labels=True, font_color='red')
plt.show() 