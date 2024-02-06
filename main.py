# main.py
from openai_definitions import get_definition, set_openai_key
from anki_integration import create_anki_flashcard

def main():
    openai_api_key = "Input API key here"
    set_openai_key(openai_api_key)

    term = input("Enter the term you want to define: ")

    definition = get_definition(term)
    if definition:
    
        deck_name = "Security+ Concepts"
        
        result = create_anki_flashcard(term, definition, deck_name=deck_name)
        if result and not result.get("error"):
            print(f"Successfully created flashcard for '{term}' in deck '{deck_name}'.")
        else:
            print(f"Failed to create flashcard. Error: {result.get('error')}")
    else:
        print("Failed to get definition.")

if __name__ == "__main__":
    main()

