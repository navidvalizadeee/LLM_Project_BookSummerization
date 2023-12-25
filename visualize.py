import networkx as nx
import matplotlib.pyplot as plt  
import csv
from Methods.graphFilters import *

nodeFile = "Data/Nodes_WO_NM_WKG_6.csv"
edgeFile = "Data/Edges_WO_NM_WKG_6.csv"
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

attributesList = GetAllNodeAttributes(nodes, "T")
print(attributesList)

attribute = "character"
# attributes = ["character", "animal"]
attributes = attributesList

tNodes = GetNodesByAttributes(nodes, "T", attributes)
print(len(tNodes))
tEdges = GetEdgesByNodes(edges, tNodes)
print(len(tEdges))
print(tNodes.keys())
# nx.draw_networkx(graph, with_labels=True, font_color='red')
pos = nx.spring_layout(graph)

newGraph = nx.Graph()
# for ndID, nd in tNodes.items():
#     newGraph.add_node(ndID, **nd)
# for edId, ed in tEdges.items():
#     newGraph.add_edge(ed["S"], ed["T"], **ed)

for ndID, nd in nodes.items():
    newGraph.add_node(ndID, **nd)
for edId, ed in edges.items():
    newGraph.add_edge(ed["S"], ed["T"], **ed)
CheckEdgeNNodesIntegirity(edges, nodes)
nx.draw_networkx(newGraph, pos=pos, with_labels=True, font_color='red', node_size=50, alpha=0.8)
plt.axis('equal')
plt.show() 