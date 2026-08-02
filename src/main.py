from src.storage import load_expenses
from src.expenses import add_expense, view_expenses, search_category, delete_expense, edit_expense
from src.reports import show_total

def main():
    """
    Run the Budget Tracker application.
    
    Display the main menu and process the user commands until the user exits.
    """
    expenses = load_expenses()                                                                   
    
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
            
if __name__ == '__main__':
    main()