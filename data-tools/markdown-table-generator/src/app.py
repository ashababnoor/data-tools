import os
import sys
from typing import Union
from json_to_md import json_to_markdown


ACCEPTED_EXTENSIONS = ['json', 'csv']

def generate_markdown(input_file: str, save_in_file: bool = True, output_file: Union[str, None] = None) -> None:
    input_file_basename = os.path.basename(input_file)
    input_file_extension = input_file.split(".")[-1]
    if input_file_basename == input_file_extension:
        print(f"Error: Input file doesn't have an extenion")
        print(f"Input file: {input_file}")
        sys.exit()
    
    if input_file_extension not in ACCEPTED_EXTENSIONS:
        print(f"Error: Input file type is unsupported")
        print(f"Input file: {input_file}")
        print()
        print(f"Supported file types: {', '.join(ACCEPTED_EXTENSIONS).upper()}")
        sys.exit()
    
    if output_file is None:
        output_file = os.path.basename(input_file).replace(input_file_extension, "md")
        
    # TODO: Finish rest of the code
    

if __name__ == "__main__":
    generate_markdown("hello.c")