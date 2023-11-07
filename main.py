import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
# mainTextPath = "Data/As I Lay Dying.txt"
mainTextPath = "Data\As I Lay Dying.txt"
# mainText = open(mainTextPath, "r").read()

messageHistory = []
systemContent = """
Identify and list all the unique entities from the given text, make sure you don't miss anything.
Important entities are charachters, relations, events, locations, objects, and concepts.
Also a string in json format is always provided. if it is empty it mean no data is extracted yet.
"""
systemMessage = {"role": 'system', "content":systemContent}
messageHistory.append(systemMessage)
def extract_entities(text):
    try:
        response = openai.ChatCompletion.create(
          model='gpt-3.5-turbo',
          messages=[{'role': 'system', 'content': f""},
                     {'role': 'user', 'content': f"{text}"}]
        )
        # Extract the entities from the response
        choices = response['choices']
        firstMessage = choices[0].message.content
        role = choices[0].message.role
        print(role, "\n", firstMessage)

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
paraphsPerMessage = 50
historyParaphsPerMessage = round(paraphsPerMessage * 0.1)
maxParaphParsed = 51

for i in range(0, paraCount, paraphsPerMessage):
    if i >= maxParaphParsed:
        break
    content = ""
    for j in range(i):
        content += paragraphs[j] + "\n"
    newMessage = {"role": 'user', "content": content}
    messageHistory.append(newMessage)
    extract_entities(content)
