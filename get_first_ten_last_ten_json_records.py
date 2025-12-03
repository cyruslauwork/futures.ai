import json

def get_head_and_tail(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Ensure data is a list
    if isinstance(data, list):
        head = data[:10]  # Get the first 10 items
        tail = data[-10:]  # Get the last 10 items
    else:
        raise ValueError("JSON data is not a list.")

    return head, tail

# Example usage
if __name__ == "__main__":
    json_file_path = 'spy_1min_regularhours_truncated_preprocessed.json'  # Replace with your JSON file path
    head, tail = get_head_and_tail(json_file_path)

    print("Head (first 10 items):")
    print(head)
    print("\nTail (last 10 items):")
    print(tail)