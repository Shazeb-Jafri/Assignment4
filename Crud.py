from Data_Persistence import load_data, save_data
import json

data = load_data()

def create_or_update_entry(item_id, new_item):
    found = False
    for item in data:
        if item['id'] == item_id:
            item.update(new_item)
            found = True
            break
    if not found:
        data.append(new_item)
    save_data(data)

def delete_entry(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    save_data(data)

def display_data():
    """Display the JSON data."""
    print(json.dumps(data, indent=2))

