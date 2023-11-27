from fuzzywuzzy import fuzz
import json
import csv


def compare_schemas(schema1, schema2, save_in_file=True, common_file="common_columns.csv", similar_file="similar_columns.csv", uncommon_file="uncommon_columns.csv"):
    common_columns = []
    similar_columns = []
    uncommon_columns = []
    
    for col1 in schema1:
        for col2 in schema2:
            if col1['name'] == col2['name'] and col1['type'] == col2['type']:
                common_columns.append((col1['name'], col1['type']))
            elif col1['type'] == col2['type'] and fuzz.ratio(col1['name'], col2['name']) > 80:
                similar_columns.append((col1['name'], col2['name'], col1['type']))
    
    # Find uncommon columns
    all_columns = set((col['name'], col['type'], "schema1") for col in schema1) | set((col['name'], col['type'], "schema2") for col in schema2)
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