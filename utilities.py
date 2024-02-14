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