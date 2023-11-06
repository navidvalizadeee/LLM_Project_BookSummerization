import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
mainTextPath = "Data/As I Lay Dying.txt"
mainText = open(mainTextPath, "r").read()

def extract_entities(text):
    try:
        response = openai.ChatCompletion.create(
          model='gpt-3.5-turbo',
          messages=[{'role': 'system', 'content': f"Identify and list all the unique entities from the following, make sure you don't miss anything."},
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
print(paragraphs[2])
# Now 'paragraphs' is a list containing each paragraph as an element

