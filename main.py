import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_entities(text):
    try:
        # Call the OpenAI API to extract entities from the text
        response = openai.Completion.create(
          engine="text-davinci-003",  # or the latest engine available
          prompt=f"Identify and list all the unique entities from the following text:\n\n{text}",
          max_tokens=150
        )

        # Extract the entities from the response
        entities = response.choices[0].text.strip().split('\n')

        return entities
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example text to analyze
text_to_analyze = "Alice is a data scientist at Initech. She works with Bob, a software engineer."

# Extract entities
entities = extract_entities(text_to_analyze)

# Now entities contains a list of entities extracted from the text
print("Extracted Entities:", entities)