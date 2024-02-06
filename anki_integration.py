# anki_integration.py
import requests

def create_anki_flashcard(front, back, deck_name="Default", model_name="Basic"):
    try:
        url = "http://localhost:8765"
        payload = {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": deck_name,
                    "modelName": model_name,
                    "fields": {
                        "Front": front,
                        "Back": back,
                    },
                    "tags": ["generated"],
                }
            }
        }
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"An error occurred while creating flashcard: {e}")
        return None

