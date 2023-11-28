import json
import sys
from tabulate import tabulate


def json_to_markdown(json_file: str) -> str:
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
        print("Error: Input JSON data should be a list of dictionaries.")
        sys.exit()
    
    md_table = tabulate(data, headers="keys", tablefmt="pipe")
    
    return md_table


def main():
    md_table = json_to_markdown('data/input.json')
    print(md_table)
    
if __name__ == "__main__":
    main()