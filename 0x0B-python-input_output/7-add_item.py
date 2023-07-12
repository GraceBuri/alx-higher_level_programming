#!/usr/bin/python3
import sys
import json


def save_to_json_file(items, filename):
    """ Function that saves a list of items to a JSON file

    Args:
        items: list of items
        filename: filename

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(items, f)


def load_from_json_file(filename):
    """ Function that loads a list of items from a JSON file

    Args:
        filename: filename

    Returns:
        list of items

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    items = []
    for arg in sys.argv[1:]:
        items.append(arg)
    save_to_json_file(items, "add_item.json")
