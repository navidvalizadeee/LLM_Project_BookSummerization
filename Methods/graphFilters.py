import networkx as nx

def GetAllNodeAttributes(nodes: dict, attributeKey: str)-> list:
    attributes = list()

    for nodeid, nodevalues in nodes.items():
        attribute = nodevalues[attributeKey]
        if attribute is not None:
            attributes.append(attribute)
    attributes = list(set(attributes))
    return attributes

def GetNodesByAttribute(nodes: dict, attributeKey: str, attributeValue: str)-> dict:
    newNodes = dict()

    for nodeid, nodevalues in nodes.items():
        attribute = nodevalues[attributeKey]
        if attribute is not None and attribute == attributeValue:
            newNodes.setdefault(nodeid, nodevalues)
    return newNodes

def GetNodesByAttributes(nodes: dict, attributeKey: str, attributeValues: list)-> dict:
    newNodes = dict()

    for nodeid, nodevalues in nodes.items():
        attribute = nodevalues[attributeKey]
        if attribute is not None and attribute in attributeValues:
            newNodes.setdefault(nodeid, nodevalues)
    return newNodes

def GetEdgesByNodes(edges: list, nodes: list)-> dict:
    newEdges = dict()
    counter = 0
    for edgId, edValues in edges.items():
        source = edValues["S"]
        target = edValues["T"]
        if source in nodes and target in nodes:
            # print(f"source: {source}, target: {target}, data: {data}")
            newEdges.setdefault(counter, edValues)
            counter += 1
            # print(f"source: {source}, target: {target}, counter: {counter}")
    return newEdges

def GetRouteFromNodeToNode(graph: nx.graph, source: str, target: str)-> list:
    route = list()
    hasPath = nx.has_path(graph, source=source, target=target)
    if hasPath:
        route = nx.shortest_path(graph, source=source, target=target)
    return route

def CheckEdgeNNodesIntegirity(edges: dict, nodes: dict)-> bool:
    counter = 0
    for edgId, edValues in edges.items():
        source = edValues["S"]
        target = edValues["T"]
        if source not in nodes or target not in nodes:
            counter += 1
            if source not in nodes:
                print(f"source: {source} not in nodes")
            if target not in nodes:
                print(f"target: {target} not in nodes")
    print(f"counter: {counter}")
    if counter > 0:
        return False
    else:
        return True