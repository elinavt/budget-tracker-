import pandas as pd

expenses = []

def add_expense(expenses): 
    while True:
        try:
            date = pd.to_datetime(input('Enter the date of the expense: '), dayfirst=True).strftime('%Y-%m-%d')
            break
        except ValueError:
            print('Please enter a valid date.')
    while True:
        try:       
            amount =  float(input('Enter the amount of expense: '))   
            if amount > 0:
                break
            print('amount must be greater than 0.')
        except ValueError:
            print('Please enter a valid number.')
    while True:
        category = input('Enter the category of expense: ').strip().title()
        if category:
            break
        print('Category cannot be empty.')
    while True:
        description = input('Enter the description of expense: ').strip()
        if description:
            break
        print('Description cannot be empty.')
    expense = {
        'date' : date,
        'amount' : amount,
        'category' : category,
        'description' : description
    }         
    expenses.append(expense)
    print('Expense added.')
  
  
def view_expenses(expenses):
    if not expenses:
        print('No expenses recorded.')  
        return       
    for i, expense in enumerate(expenses, start=1):
        print(f'Expense #{i}')
        print(f"Date : {expense['date']}")
        print(f"Category : {expense['category']}")
        print(f"Amount : {expense['amount']:.2f}")
        print(f"Description : {expense['description']}")
        print('-' * 30)
        
        
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
while True:
    print('''
    ==== Budget Tracker ====
        
    1. Add expense
    2. View expenses
    3. Show total spending
    4. Search by category
    5. Exit
    
    ''')
    choice = input('Choice: ')  
    
    if choice == '1':
        add_expense(expenses)
        print()
    elif choice == '2':
        view_expenses(expenses) 
        print()
    elif choice == '3':
        show_total(expenses)
        print()
    elif choice == '4':
        search_category(expenses)
        print()
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice')   
        print()
        
