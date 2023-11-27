from dependency_injector import bigquery_client
from comparer import compare_schemas, generate_summary
from helper import Table
import os


def compare(config_key: str, output_folder: str = "output") -> None:
    table1, table2 = Table.get_tables_from_config(config_key)
    schema1 = bigquery_client.get_schema(table1)
    schema2 = bigquery_client.get_schema(table2)
    
    sub_output_folder = config_key + "_schema_comparison"
    output_folder = os.path.join(output_folder, sub_output_folder)

    outputs = compare_schemas(schema1, schema2, save_in_file=True, output_folder=output_folder)
    common_columns, similar_columns, uncommon_columns = outputs
    
    generate_summary(table1, table2, common_columns, similar_columns, uncommon_columns, output_folder=output_folder)


def main():
    config_key = ""
    compare(config_key)


if __name__ == "__main__":
    main()