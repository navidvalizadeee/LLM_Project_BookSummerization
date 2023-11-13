import openai
import os
import json
import pprint
import networkx as nx
import matplotlib.pyplot as plt

openai.api_key = os.getenv("OPENAI_API_KEY")
mainTextPath = "Data/As I Lay Dying.txt"
# mainTextPath = "Data\As I Lay Dying.txt"
# mainText = open(mainTextPath, "r").read()
INDEX = "index"
NODES = "Nodes"
EDGES = "Edges"

messageHistory = []
systemContent = """
Identify and list all the unique entities from the given text, make sure you don't miss anything.
From now on we call these entities as Nodes.
Nodes are charachters, relations, events, locations, objects, and concepts.
Node types must be mentioned in the output.
Do not include any Nodes that are not in the text.
Do not use prenouns or pronouns, use the full name of the Nodes. 
This is a Node sample: {"id": "Ada", "T": "charachter"}
Also a string in json format is always provided. if it is empty it mean no data is extracted yet.
You must also return the Nodes in JSON format.
Moreover, show connections between the Nodes as Edges by using the following format:
{"S": "Node1_id", "T": "Node2_id", "R": "Relation1", "ST": "positive"}
"S" is for source, "T" is for target, "R" is for relation, "ST" is for sentiment.
Relations are verbs, adjectives, and adverbs, none of them are unique names, all of them are general terms.
"""

systemMessage = {"role": 'system', "content": systemContent}

messageHistory.append(systemMessage)
def extract_entities(messages):
    try:
        response = openai.ChatCompletion.create(
        #   model='gpt-3.5-turbo',
          model='gpt-3.5-turbo-1106',
        #   model='gpt-4-1106-preview',
          messages=messages,
          temperature=0,
        #   max_tokens=1000,
          response_format= {'type': 'json_object'}
        )
        # Extract the entities from the response
        choices = response['choices']
        firstMessage = choices[0].message.content
        role = choices[0].message.role
        # print(role, "\n", firstMessage)
        return response

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# entities = extract_entities(text_to_analyze)
paragraphs = []
with open(mainTextPath, 'r') as file:
    paragraph = []
    for line in file:
        if line.strip() == '':  # Check for blank lines
            if paragraph:
                paragraphs.append('\n'.join(paragraph))
                paragraph = []
        else:
            paragraph.append(line.strip())
    if paragraph:  # Add the last paragraph if the file doesn't end with a blank line
        paragraphs.append('\n'.join(paragraph))

paraCount = len(paragraphs)
paraphsPerMessage = 30
historyParaphsPerMessage = round(paraphsPerMessage * 0.1)
maxParaphParsed = 300
nodes = dict()
edges = dict()
idx = 0
for i in range(0, paraCount, paraphsPerMessage):
    if i >= maxParaphParsed or i >= paraCount:
        break
    print(f"sending paragraphs {i} to {i + paraphsPerMessage} out of {paraCount}")
    content = ""
    for j in range(i, i + paraphsPerMessage):
        content += paragraphs[j] + "\n"
    newMessage = {"role": 'user', "content": content}
    messages = messageHistory + [newMessage]
    print("")
    print("sending request to openai")
    response = extract_entities(messages)
    try:
        jsonRes = json.loads(response.choices[0].message.content)
        nds = jsonRes[NODES]
        eds = jsonRes[EDGES]
        for nd in nds:
            if nd["id"] not in nodes:
                nodes[nd["id"]] = nd
        for ed in eds:
            edges[idx] = ed
            idx += 1
        # pprint.pprint(jsonRes)
        print(f"node count: {len(nodes)}, edge count: {len(edges)}")
    except Exception as e:
        print(response)
        print("could not parse json")
        print(e)

graph = nx.Graph()
for nd in nodes:
    graph.add_node(nd, **nodes[nd])
for ed in edges:
    graph.add_edge(edges[ed]["S"], edges[ed]["T"], **edges[ed])

nx.draw_networkx(graph, with_labels=True)
plt.show()