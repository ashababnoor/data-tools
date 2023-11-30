from typing import Union
from dependency_injector import bigquery_client
from comparer import compare_schemas, generate_summary
from helper import Table
import os


def compare(config_key: str, output_folder: str = "output", config_file: Union[str, None] = None) -> None:
    print(f"Performing schema comparison for config key: {config_key}")
    table1, table2 = Table.get_tables_from_config(config_key, config_file_path=config_file)
    print(f"    Table 1: `{table1.get_table_id()}`")
    print(f"    Table 2: `{table2.get_table_id()}`")
    print()
    
    schema1 = bigquery_client.get_schema(table1)
    schema2 = bigquery_client.get_schema(table2)
    
    sub_output_folder = config_key + "_schema_comparison"
    output_folder = os.path.join(output_folder, sub_output_folder)

    outputs = compare_schemas(schema1, schema2, save_in_file=True, output_folder=output_folder)
    common_columns, similar_columns, uncommon_columns = outputs
    
    generate_summary(table1, table2, common_columns, similar_columns, uncommon_columns, output_folder=output_folder)
    print("Schema comparison output saved in the following location:")
    print(f"    {os.path.abspath(output_folder)}")


def main():
    config_key = "food_tables"
    compare(config_key)


if __name__ == "__main__":
    main()