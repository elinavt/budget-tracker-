from src.inputs import get_date, get_amount, get_category, get_description
from src.storage import save_expenses

def has_expenses(expenses: list[dict]) -> bool:
    """Return True if list of expenses is not empty, otherwise print a message."""
    if not expenses:
        print('No expenses recorded.')
        return False
    return True

def add_expense(expenses: list[dict]) -> None: 
    """
    Prompt the user for expense information and add it to the list of expenses.
    
    Save the updated expenses list.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    expense = {
        'date' : get_date(),
        'amount' : get_amount(),
        'category' : get_category(),
        'description' : get_description()
    }
    expenses.append(expense)
    print('Expense added.')
    save_expenses(expenses)
  

def display_expense(expense: dict) -> None:
    """
    Display the details of an expense.
    
    Args:
        expense: A dictionary of expense information.
    """
    print(f"Date: {expense['date']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: {expense['amount']:.2f}")
    print(f"Description: {expense['description']}")  
    print('-' * 30)
  
      
def view_expenses(expenses: list[dict]) -> None:
    """
    Display the list of expenses.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    if not has_expenses(expenses):  
        return   
    for i, expense in enumerate(expenses, start=1):
        print(f'Expense #{i}')
        display_expense(expense)   

        
def search_category(expenses: list[dict]) -> None:
    """
    Prompt the user for a category and display the matching expenses.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    if not has_expenses(expenses):
        return
    category = input('Enter category: ').strip()
    category_expenses = [
        expense for expense in expenses
        if expense['category'].casefold() == category.casefold()
    ]
    if not category_expenses:
        print(f'No expenses found in category "{category}".')
    else: 
        view_expenses(category_expenses)   
        
        
def delete_expense(expenses: list[dict]) -> None:
    """
    Prompt the user to select an expense and delete it.
    
    Save the updated expenses list.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    if not has_expenses(expenses):
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
        deleted = expenses.pop(expense_num - 1)
        save_expenses(expenses)
        print(f'Expense #{expense_num} deleted:')
        display_expense(deleted)
    else:
        print('Deletion cancelled.')                                                       


def edit_expense(expenses: list[dict]) -> None:
    """
    Prompt the user to select an expense and edit one or more fields.
    
    Save the updated list after each edit.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    if not has_expenses(expenses):
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