from tabulate import tabulate
import re

def prettify_markdown_table(markdown_table: str) -> str:
    """
    Prettify markdown table

    Args:
        markdown_table (str): The input markdown table that is to be prettified

    Returns:
        str: Preffitified markdown table.
    """
    # Split the input string into rows
    rows = markdown_table.strip().split('\n')

    # Split each row into columns
    table_data = [row.split('|') for row in rows]
        
    rows_to_delete = []
    for index, row in enumerate(table_data):
        if re.sub(r'[^a-zA-Z0-9]', "", "".join(row)).strip() == "":
            rows_to_delete.append(index)
    
    for index in sorted(rows_to_delete, reverse=True):
        table_data.pop(index)

    # Remove leading and trailing whitespaces from each column
    table_data = [[col.strip() for col in row] for row in table_data]

    # Remove the first and last elements (empty strings) from each row
    table_data = [row[1:-1] for row in table_data]

    # Use tabulate to create a pretty table
    pretty_table = tabulate(table_data, headers="firstrow", tablefmt="pipe")

    return pretty_table

def main():
    markdown_input = """
    | Name  | Age | City    |
    |-------|-----|---------|
    | Alice | 25  | New York|
    | Bob   | 30  | London  |
    | Carol | 22  | Paris   |
    """

    prettified_table = prettify_markdown_table(markdown_input)
    print(prettified_table)
    
if __name__ == "__main__":
    main()