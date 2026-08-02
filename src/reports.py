def show_total(expenses: list[dict]) -> None:
    """
    Calculate and display the total amount of all the expenses.
    
    Args:
        expenses: A list of expense dictionaries.
    """
    if not expenses:
        print('No expenses recorded.')
        return         
    total = sum(expense['amount'] for expense in expenses)
    print(f'Total spending: {total:.2f}')         