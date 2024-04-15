import json

json_file_path = 'Books.json'


def load_data():
    """Load data from the JSON file."""
    try:
        with open(json_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Save data to the JSON file."""
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)
