from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_NAME = BASE_DIR / 'data' / 'expenses.csv'

FIELDS = ('date', 'amount', 'category', 'description')

def load_expenses() -> list[dict]:
    """
    Load expenses from the CSV file.
     
    Skip the invalid rows.
   
    Returns:
        list[dict]: A list of expense dictionaries.
    """
    if not FILE_NAME.exists():
        return []
    required_fields = set(FIELDS)
    with open(FILE_NAME, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not required_fields.issubset(reader.fieldnames):
            print('CSV file format is invalid.')
            return []
        expenses = []
        for row_num, row in enumerate(reader, start=2):
            try:
                row['amount'] = float(row['amount'])
                expenses.append(row)
            except ValueError:
                print(f'Warning: skipping invalid data on CSV row {row_num}')
                continue
    return expenses
    
       
def save_expenses(expenses: list[dict]) -> None:
    """
    Save expenses to the CSV file.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    FILE_NAME.parent.mkdir(exist_ok=True)
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as file:
        fieldnames = FIELDS
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)