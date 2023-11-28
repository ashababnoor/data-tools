import os
import sys
from typing import Union
from json_to_md import json_to_markdown
from csv_to_md import csv_to_markdown


ACCEPTED_EXTENSIONS = ['json', 'csv']

def generate_markdown(input_file: str, save_in_file: bool = True, output_file: Union[str, None] = None) -> None:
    INPUT_FILE_NAMES_TO_BE_CHANGED = ['input']
    
    if not os.path.exists(input_file):
        print(f"Error: input file does not exist in path {input_file}")
        print(f"    Absolute path: {os.path.abspath(input_file)}")
        sys.exit()
    
    input_file_dir = os.path.dirname(input_file)
    input_file_basename = os.path.basename(input_file)
    input_file_extension = input_file_basename.split(".")[-1]
    input_file_name = input_file_basename.split(".")[0]
    
    if input_file_basename == input_file_extension:
        print(f"Error: Input file doesn't have an extenion")
        print(f"Input file: {input_file}")
        sys.exit()
    
    if input_file_extension.lower() not in ACCEPTED_EXTENSIONS:
        print(f"Error: Input file type is unsupported")
        print(f"Input file: {input_file}")
        print()
        print(f"Supported file types: {', '.join(ACCEPTED_EXTENSIONS).upper()}")
        sys.exit()
    
    markdown_table = ""
    if input_file_extension.lower() == "json":
         markdown_table = json_to_markdown(json_file=input_file)
    elif input_file_extension.lower() == "csv":
         markdown_table = csv_to_markdown(csv_file=input_file)


    if not save_in_file:
        return markdown_table
    
    if output_file is None:
        if input_file_name.lower() in INPUT_FILE_NAMES_TO_BE_CHANGED:
            input_file_name = "output"
        
        output_file = os.path.join(input_file_dir, f"{input_file_name}.md")
    
    with open(output_file, 'w') as file:
        file.writelines(markdown_table)
        
    return markdown_table


if __name__ == "__main__":
    markdown_table = generate_markdown("data/input.json")