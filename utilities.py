import json

def load_data_from_file(json_filename):
    """
    Loads data from a JSON file.

    Parameters:
    - json_filename (str): The name of the JSON file to load from (excluding the ".json" extension).

    Returns:
    - data_list (list): The loaded data as a list. If an error occurs during loading, an empty list is returned.
    """
    data_list = []
    with open(f"data/{json_filename}.json") as f:
        try:
            data_list = json.load(f)
            return data_list
        except:
            return data_list


def save_data_to_file(json_filename, data_list=[]):
    """
    Saves data to a JSON file.

    Parameters:
    - json_filename (str): The name of the JSON file to save to (excluding the ".json" extension).
    - data_list (list): The data to be saved to the file. Defaults to an empty list if not provided.

    Returns:
    - None
    """
    with open(f"data/{json_filename}.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)


def append_data_to_file(json_filename, data):
    """
    Appends data to a JSON file.

    Parameters:
    - json_filename (str): The name of the JSON file to append to (excluding the ".json" extension).
    - data: The data to be appended to the file.

    Returns:
    - None
    """
    data_list = load_data_from_file(json_filename)
    data_list.append(data)
    save_data_to_file(json_filename, data_list)


def print_json(input_dictionary, indent=0):
    """
    Prints a dictionary in a structured format.

    Parameters:
    - input_dictionary (dict): The dictionary to be printed.
    - indent (int): The indentation level. Defaults to 0.

    Returns:
    - None
    """
    # Loop through dictionary values
    for key, value in input_dictionary.items():
        # If the value that is being looped through is a dictionary, recursively call this print function
        if isinstance(value, dict):
            print(f"{'  ' * indent}\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m:")
            print_json(value, indent + 1)
        # If the value that is being looped through is a list, loop through the list
        elif isinstance(value, list):
            print(f"{'  ' * indent}\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m:")
            for index, item in enumerate(value):
                # If there's a dictionary inside the list, recursively call this function to print the key, value pairs for the dictionary
                if isinstance(item, dict):
                    print_json(item, indent + 1)
                else:
                    print(f"{'  ' * indent}\033[1;97m#{index+1}\033[00m: {item}")
        else:
            print(f"{'  ' * indent}\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m: {value}")


def print_value_for_key(input_dictionary, target_key, current_key=None):
    """
    Prints the value associated with a specific key in a nested dictionary.

    Parameters:
    - input_dictionary (dict): The dictionary to search for the key.
    - target_key (str): The key to search for.
    - current_key (str): The current key being traversed. Defaults to None.

    Returns:
    - None
    """
    for key, value in input_dictionary.items():
        if isinstance(value, dict):
            # Recursively call this function if a dictionary is found where the key could be located
            current_key = key if current_key is None else current_key
            print_value_for_key(value, target_key, current_key)
        elif isinstance(value, list):
            # Loop through list items if a list is found
            for item in value:
                if isinstance(item, dict) or isinstance(item, list):
                    # Recursively call this function if a dictionary is found inside the list
                    print_value_for_key(item, target_key, current_key)
        elif key == target_key:
            print(f"\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m: {value}")