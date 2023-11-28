import csv
import sys
from tabulate import tabulate


def csv_to_markdown(csv_file: str) -> str:
    data = []
    
    # Read JSON data from file
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    md_table = tabulate(data, headers="firstrow", tablefmt="pipe")
    
    return md_table


def main():
    md_table = csv_to_markdown('data/input.csv')
    print(md_table)
    
if __name__ == "__main__":
    main()