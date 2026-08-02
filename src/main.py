from pathlib import Path
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_NAME = BASE_DIR / 'data' / 'expenses.csv'

def load_expenses(FILE_NAME):
    if not FILE_NAME.exists():
        return []
    required_fields = {'date', 'amount', 'category', 'description'}
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
    
expenses = load_expenses(FILE_NAME) 
       
def save_expenses(expenses):
    FILE_NAME.parent.mkdir(exist_ok=True)
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['date', 'amount', 'category', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def get_date():
    while True:
        try:
            date = datetime.strptime(
                input('Enter the date of the expense (DD/MM/YYYY): '), '%d/%m/%Y'
                ).strftime('%Y-%m-%d')
            break
        except ValueError:
            print('Please enter a valid date.')
    return date
    

def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount of the expense: '))
            if amount > 0:
                break
            print('Amount must be greater than zero.')
        except ValueError:
            print('Please enter a valid number.')  
    return amount
    
    
def get_category():
    while True:
        category = input('Enter the category of the expense: ').strip().title()
        if category:
            break
        print('Category cannot be empty.')
    return category
    
    
def get_description():
    while True:
        description = input('Enter the description of the expense: ').strip()
        if description:
            break
        print('Description cannot be empty.')
    return description


def add_expense(expenses): 
    expense = {
        'date' : get_date(),
        'amount' : get_amount(),
        'category' : get_category(),
        'description' : get_description()
    }
    expenses.append(expense)
    print('Expense added.')
    save_expenses(expenses)
  

def display_expense(expense):
    print(f"Date: {expense['date']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: {expense['amount']:.2f}")
    print(f"Description: {expense['description']}")  
    print('-' * 30)
  
      
def view_expenses(expenses):
    if not expenses:
        print('No expenses recorded.')  
        return   
    for i, expense in enumerate(expenses, start=1):
        print(f'Expense #{i}')
        display_expense(expense)
        
        
def show_total(expenses):
    if not expenses:
        print('No expenses recorded.')  
        return         
    total = sum(expense['amount'] for expense in expenses)
    print(f'Total spending: {total:.2f}')            

        
def search_category(expenses):
    if not expenses:
        print('No expenses recorded')
        return
    category = input('Enter category: ').strip().title()
    category_expenses = [
        expense for expense in expenses
        if expense['category'] == category
    ]
    if not category_expenses:
        print(f'No expenses found in category "{category}".')
    else: 
        view_expenses(category_expenses)   
        
        
def delete_expense(expenses):
    if not expenses:
        print('No expenses recorded.')
        return
    view_expenses(expenses)
    while True:
        try: 
            expense_num = int(input('Enter the expense number you want to delete: '))
            if 1 <= expense_num <= len(expenses):
                break
            print('Please enter a valid expense number.')
        except ValueError:
            print('Please enter a valid number.')
    confirm = input(f'Delete the Expense #{expense_num}? (y/n): ').strip().lower()
    if confirm == 'y':
        expenses.pop(expense_num - 1)
        save_expenses(expenses)
        print('Expense deleted.')
    else:
        print('Deletion cancelled.')                                                       


def edit_expense(expenses):
    if not expenses:
        print('No expenses recorded.')
        return
    view_expenses(expenses)
    while True:
        try:
            expense_num = int(input('Enter the expense number you want to edit: '))
            if 1 <= expense_num <= len(expenses):
                break
            print('Please enter a valid expense number.')
        except ValueError:
            print('Please enter a valid number.')
    expense = expenses[expense_num - 1]
    actions = {
        '1' : ('date', get_date),
        '2' : ('amount', get_amount),
        '3' : ('category', get_category),
        '4' : ('description', get_description)
    }
    while True:
        choice = input('''
    What do you want to edit?
    1. date
    2. amount
    3. category
    4. description
    5. Exit (done editing)
    ''') 
        if choice == '5':
            print('Exiting edit mode.')
            break
        action = actions.get(choice)
        if action:
            field, func = action
            print(f'Current {field}: {expense[field]}')
            expense[field] = func()
            save_expenses(expenses)
            print(f'{field.title()} updated.')
            print(f'Expense #{expense_num}')
            display_expense(expense)
            print()
        else:
            print('Please enter a valid choice.')  
            print()                                                      
                                                                                         
    
actions = {
    '1' : add_expense,
    '2' : view_expenses,
    '3' : show_total,
    '4' : search_category,
    '5' : delete_expense,
    '6' : edit_expense
}                                                                                                                     
                                                                                                                                  
while True:
    print('''
    ==== Budget Tracker ====
        
    1. Add expense
    2. View expenses
    3. Show total spending
    4. Search by category
    5. Delete expense
    6. Edit expense
    7. Exit
    
    ''')
    choice = input('Choice: ')  
    if choice == '7':
        print('Goodbye!')
        break
    func = actions.get(choice)
    if func:
        func(expenses)
        print()    
    else:
        print('Please enter a valid choice.')
        print()