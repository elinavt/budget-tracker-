from datetime import datetime

def get_date() -> str:
    """
    Prompt the user for a valid expense date.
    
    Returns:
        str: The validated expense date.
    """
    while True:
        try:
            date = datetime.strptime(
                input('Enter the date of the expense (DD/MM/YYYY): '), '%d/%m/%Y'
                ).strftime('%Y-%m-%d')
            break
        except ValueError:
            print('Please enter a valid date.')
    return date
    

def get_amount() -> float:
    """
    Prompt the user for a positive expense amount.
    
    Returns:
        float: The validated expense amount.
    """
    while True:
        try:
            amount = float(input('Enter the amount of the expense: '))
            if amount > 0:
                break
            print('Amount must be greater than zero.')
        except ValueError:
            print('Please enter a valid number.')  
    return amount
    
    
def get_category() -> str:
    """
    Prompt the user for an expense category.
    
    Returns:
        str: The expense category.
    """
    while True:
        category = input('Enter the category of the expense: ').strip()
        if category:
            break
        print('Category cannot be empty.')
    return category
    
    
def get_description() -> str:
    """
    Prompt the user for an expense description.
    
    Returns:
        str: The expense description.
    """
    while True:
        description = input('Enter the description of the expense: ').strip()
        if description:
            break
        print('Description cannot be empty.')
    return description