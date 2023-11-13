from tabulate import tabulate

def prettify_markdown_table(markdown_table):
    # Split the input string into rows
    rows = markdown_table.strip().split('\n')

    # Split each row into columns
    table_data = [row.split('|') for row in rows]
    table_data.pop(1)

    # Remove leading and trailing whitespaces from each column
    table_data = [[col.strip() for col in row] for row in table_data]

    # Remove the first and last elements (empty strings) from each row
    table_data = [row[1:-1] for row in table_data]

    # Use tabulate to create a pretty table
    pretty_table = tabulate(table_data, headers="firstrow", tablefmt="pipe")

    return pretty_table

# Example usage
markdown_input = """
| Name  | Age | City    |
|-------|-----|---------|
| Alice | 25  | New York|
| Bob   | 30  | London  |
| Carol | 22  | Paris   |
"""

prettified_table = prettify_markdown_table(markdown_input)
print(prettified_table)