from tabulate import tabulate
import csv
import sys


def _csv_to_markdown(csv_file: str) -> str:
    """
    Convert table data in CSV format to Markdown table

    Args:
        csv_file (str): Path of input file containing CSV table data

    Returns:
        str: Converted markdown table
    """
    data = []
    
    # Read CSV data from file
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    # Check if all lists are the same size
    sizes = set(len(row) for row in data)
    same_size = len(sizes) == 1
    if not same_size:
        print("Error: Input CSV data should have list of lists where all lists are the same size")
        sys.exit()
    
    md_table = tabulate(data, headers="firstrow", tablefmt="pipe")
    
    return md_table


def main():
    md_table = _csv_to_markdown('data/input.csv')
    print(md_table)
    
if __name__ == "__main__":
    main()