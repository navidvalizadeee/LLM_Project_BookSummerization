import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_entities(text):
    try:
        # Call the OpenAI API to extract entities from the text
        # response = openai.Completion.create(
        #   engine="gpt-3.5-turbo",  # or the latest engine available
        #   prompt=f"Identify and list all the unique entities from the following text:\n\n{text}",
        #   max_tokens=150
        # )

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

# Example text to analyze
text_to_analyze = "Alice is a data scientist at Initech. She works with Bob, a software engineer."

# Extract entities
entities = extract_entities(text_to_analyze)
