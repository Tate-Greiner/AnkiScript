#openai_definitions.py
import openai

def set_openai_key(api_key):
    openai.api_key = api_key

def get_definition(term):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust as necessary
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Define the term '{term}' in simple terms suitable for a flashcard."}
            ]
        )
        if response and response['choices']:
            definition = response['choices'][0]['message']['content']
            return definition.strip()
    except Exception as e:
        print(f"An error occurred while getting definition: {e}")
        return None
