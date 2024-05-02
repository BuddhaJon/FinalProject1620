import json

def save_data(filename: str, data: dict):
    """Save data to a file in JSON format."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data(filename: str) -> dict:
    """Load data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
