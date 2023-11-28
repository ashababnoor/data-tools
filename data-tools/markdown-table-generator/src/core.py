from typing import Any


def _list_of_dict_to_markdown(list_of_dict: list[dict[str, Any]]) -> str:
    markdown_table = ""
    
    # Extract headers from the first dictionary
    headers = list(list_of_dict[0].keys())
    
    # Adding table header
    markdown_table += f"| {' | '.join(headers)} |\n"
    
    # Adding table header separation
    markdown_table += f"| {' | '.join(['---' for _ in headers])} |\n"
    
    # Adding table rows
    for _dict in list_of_dict:
        row = [str(_dict[header]) for header in headers]
        markdown_table += f"| {' | '.join(row)} |\n"
    
    return markdown_table


def _list_of_list_to_markdown(list_of_list: list[list[Any]]) -> str:
    list_of_list = [
        [element.strip() for element in _list] 
        for _list in list_of_list
    ]
    markdown_table = ""
    
    # Extract headers from the first list
    headers = list_of_list.pop(0)
    
    # Adding table header
    markdown_table += f"| {' | '.join(headers)} |\n"
    
    # Adding table header separation
    markdown_table += f"| {' | '.join(['---' for _ in headers])} |\n"
    
    # Adding table rows
    for row in list_of_list:
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