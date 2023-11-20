import networkx as nx
import matplotlib.pyplot as plt  
import csv
from Methods.graphFilters import *

nodeFile = "Nodes_NO_NM_WKG_3.csv"
edgeFile = "Edges_NO_NM_WKG_3.csv"
nodes = {}
edges = {}

with open(nodeFile, newline='', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nodes[row['id']] = row

with open(edgeFile, newline='', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        edges[row['S'] + row['T']] = row

graph = nx.Graph()
for nd in nodes:
    graph.add_node(nd, **nodes[nd])
for ed in edges:
    graph.add_edge(edges[ed]["S"], edges[ed]["T"], **edges[ed])

attributesList = GetAllNodeAttributes(graph, "T")
print(attributesList)

attribute = "character"
attributes = ["character", "location", "event"]

tNodes = GetNodesByAttributes(graph, "T", attributes)
print(len(tNodes))
tEdges = GetEdgesByNodes(graph, tNodes)
print(len(tEdges))
# nx.draw_networkx(graph, with_labels=True, font_color='red')
pos = nx.spring_layout(graph)

newGraph = nx.Graph()
for nd in tNodes:
    newGraph.add_node(nd, **nodes[nd])
for ed in tEdges:
    newGraph.add_edge(ed["S"], ed["T"], **ed)
print(tEdges)
nx.draw_networkx(newGraph, pos=pos, with_labels=True, font_color='red', node_size=10, alpha=0.8)
plt.axis('equal')
plt.show() 