from fuzzywuzzy import fuzz
import csv
import os
from helper import Schema


def compare_schemas(
    schema1: Schema, 
    schema2: Schema, 
    save_in_file: bool = True, 
    common_file: str = "common_columns.csv", 
    similar_file: str = "similar_columns.csv", 
    uncommon_file: str = "uncommon_columns.csv",
    output_folder: str = "output"
) -> tuple:
    common_columns = []
    similar_columns = []
    uncommon_columns = []
    
    common_file = os.path.join(output_folder, common_file)
    similar_file = os.path.join(output_folder, similar_file)
    uncommon_file = os.path.join(output_folder, uncommon_file)
    os.makedirs(os.path.dirname(common_file), exist_ok=True)
    
    for col1 in schema1.schema:
        for col2 in schema2.schema:
            if col1.name == col2.name and col1.field_type == col2.field_type:
                common_columns.append((col1.name, col1.field_type))
            elif col1.field_type == col2.field_type and fuzz.ratio(col1.name, col2.name) > 80:
                similar_columns.append((col1.name, col2.name, col1.field_type))
    
    # Find uncommon columns
    all_columns = set((col.name, col.field_type, "schema1") for col in schema1.schema) | set((col.name, col.field_type, "schema2") for col in schema2.schema)
    uncommon_columns = all_columns - set(common_columns) - set(similar_columns)
    
    if save_in_file:
        with open(common_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Common Column", "Data Type"])
            writer.writerows(common_columns)
        
        with open(similar_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Schema 1 Column", "Schema 2 Column", "Data Type"])
            writer.writerows(similar_columns)
        
        with open(uncommon_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Column Name", "Schema", "Data Type"])
            writer.writerows(uncommon_columns)
    
    return common_columns, similar_columns, list(uncommon_columns)