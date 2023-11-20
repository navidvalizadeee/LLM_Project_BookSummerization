import networkx as nx

def GetAllNodeAttributes(graph: nx.graph, attributeKey: str)-> list:
    attributes = list()

    for node, data in graph.nodes(data=True):
        attribute = data.get(attributeKey)
        if attribute is not None:
            attributes.append(attribute)
    attributes = list(set(attributes))
    return attributes

def GetNodesByAttribute(graph: nx.graph, attributeKey: str, attributeValue: str)-> list:
    nodes = list()

    for node, data in graph.nodes(data=True):
        attribute = data.get(attributeKey)
        if attribute is not None and attribute == attributeValue:
            nodes.append(node)
    return nodes

def GetNodesByAttributes(graph: nx.graph, attributeKey: str, attributeValues: list)-> list:
    nodes = list()
    for node, data in graph.nodes(data=True):
        attribute = data.get(attributeKey)
        if attribute is not None and attribute in attributeValues:
            nodes.append(node)
    return nodes

def GetEdgesByNodes(graph: nx.graph, nodes: list)-> list:
    edges = list()
    for source, target, data in graph.edges(data=True):
        if source in nodes and target in nodes:
            # print(f"source: {source}, target: {target}, data: {data}")
            edges.append(data)
    return edges

def RemoveNodesByAttribute(graph: nx.graph, attributeKey: str, attribute: str)-> nx.graph:
    pass