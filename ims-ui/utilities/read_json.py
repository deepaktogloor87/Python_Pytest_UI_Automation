import json


def read_and_parse_json(filename):
    """Read a JSON file and return a parsed dictionary."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
