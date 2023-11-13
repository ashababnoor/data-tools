import json
from prettify_table import prettify_markdown_table

def json_to_markdown(json_file: str, output_file: str, prettify: bool = True) -> None:
    # Read JSON data from file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Check if data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input JSON data should be a list of dictionaries.")

    # Extract headers from the first dictionary
    headers = list(data[0].keys())

    # Generate markdown table
    markdown_table = f"| {' | '.join(headers)} |\n| {' | '.join(['---' for _ in headers])} |\n"
    for item in data:
        row = [str(item[header]) for header in headers]
        markdown_table += f"| {' | '.join(row)} |\n"
        
    if prettify:
        markdown_table = prettify_markdown_table(markdown_table)

    # Write the markdown table to the output file
    with open(output_file, 'w') as file:
        file.write(markdown_table)

# Example Usage
json_to_markdown('data/input.json', 'data/output.md')