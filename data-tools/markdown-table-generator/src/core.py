from typing import Any
import sys


def _list_of_dict_to_markdown(list_of_dicts: list[dict[str, Any]]) -> str:
    """
    Converts list of dictionaries into Markdown format table

    Args:
        list_of_dict (list[dict[str, Any]]): List of dictionaries

    Returns:
        str: Converted markdown table
    """
    
    # Check if all dictionaries have the same number of keys
    sizes = set(len(row) for row in list_of_dicts)
    same_size = len(sizes) == 1
    if not same_size:
        print("Error: Input data should have list of dictionaries where all dictionaries are the same size")
        sys.exit()

    # Check if all dictionaries have the same keys
    all_keys = [set(row.keys()) for row in list_of_dicts]
    same_keys = all(all_keys[0] == keys for keys in all_keys[1:])
    if not same_keys:
        print("Error: Input data should have list of dictionaries where all dictionaries have the same keys")
        sys.exit()
    
    markdown_table = ""
    
    # Extract headers from the first dictionary
    headers = list(list_of_dicts[0].keys())
    
    # Adding table header
    markdown_table += f"| {' | '.join(headers)} |\n"
    
    # Adding table header separation
    markdown_table += f"| {' | '.join(['---' for _ in headers])} |\n"
    
    # Adding table rows
    for _dict in list_of_dicts:
        row = [str(_dict[header]) for header in headers]
        markdown_table += f"| {' | '.join(row)} |\n"
    
    return markdown_table


def _list_of_list_to_markdown(list_of_lists: list[list[Any]]) -> str:
    """
    Converts list of lists into Markdown format table

    Args:
        list_of_list (list[list[Any]]): List of lists

    Returns:
        str: Converted markdown table
    """
    # Check if all lists are the same size
    sizes = set(len(row) for row in list_of_lists)
    same_size = len(sizes) == 1
    if not same_size:
        print("Error: Input data should have list of lists where all lists are the same size")
        sys.exit()
    
    list_of_lists = [
        [element.strip() for element in _list] 
        for _list in list_of_lists
    ]
    markdown_table = ""
    
    # Extract headers from the first list
    headers = list_of_lists.pop(0)
    
    # Adding table header
    markdown_table += f"| {' | '.join(headers)} |\n"
    
    # Adding table header separation
    markdown_table += f"| {' | '.join(['---' for _ in headers])} |\n"
    
    # Adding table rows
    for row in list_of_lists:
        markdown_table += f"| {' | '.join(row)} |\n"
    
    return markdown_table


def main():
    import json
    import csv
    
    with open("data/input.json", 'r') as file:
        json_data = json.load(file)
    
    md_table = _list_of_dict_to_markdown(json_data)
    print(md_table)
    
    print()
    
    csv_data = []
    with open("data/input.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_data.append(row)
        
    md_table = _list_of_list_to_markdown(csv_data)
    print(md_table)

    
if __name__ == "__main__":
    main()