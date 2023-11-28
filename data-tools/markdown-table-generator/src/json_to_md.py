from tabulate import tabulate
import json
import sys


def _json_to_markdown(json_file: str) -> str:
    """
    Convert list of dictionaries in JSON format to Markdown table

    Args:
        json_file (str): Path of input file containing JSON schema data

    Returns:
        str: Converted markdown table
    """
    
    # Read JSON data from file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Check if data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        print("Error: Input JSON data should be a list of dictionaries")
        sys.exit()
    
    # Check if all dictionaries have the same number of keys
    sizes = set(len(row) for row in data)
    same_size = len(sizes) == 1
    if not same_size:
        print("Error: Input JSON data should have list of dictionaries where all dictionaries are the same size")
        sys.exit()

    # Check if all dictionaries have the same keys
    all_keys = [set(row.keys()) for row in data]
    same_keys = all(all_keys[0] == keys for keys in all_keys[1:])
    if not same_keys:
        print("Error: Input JSON data should have list of dictionaries where all dictionaries have the same keys")
        sys.exit()
    
    md_table = tabulate(data, headers="keys", tablefmt="pipe")
    
    return md_table


def main():
    md_table = _json_to_markdown('data/input.json')
    print(md_table)
    
if __name__ == "__main__":
    main()