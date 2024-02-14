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