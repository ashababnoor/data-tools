def _list_of_dict_to_markdown(list_of_dict: list[dict[str, str]]) -> str:
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


def main():
    import json
    
    with open("data/input.json", 'r') as file:
        data = json.load(file)
        
    md_table = _list_of_dict_to_markdown(data)
    print(md_table)
    

if __name__ == "__main__":
    main()