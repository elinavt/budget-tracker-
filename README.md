# Budget Tracker

A command-line budget tracking application built with Python.

This project allows users to record, view, search, edit, and delete expenses. Data is stored persistently in a CSV file. The application uses a modular structure to practice software engineering principles such as separation of concerns, reusable functions, and clean code organization.

## Features

- Add new expenses
- View all recorded expenses
- Search expenses by category
- Edit existing expenses
- Delete expenses
- Calculate total spending
- Persistent CSV data storage
- Input validation for:
  - Dates
  - Expense amounts
  - Categories
  - Descriptions

## Project Structure

```text
budget-tracker-/
│
├── data/
│   └── expenses.csv
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── expenses.py
│   ├── inputs.py
│   ├── reports.py
│   └── storage.py
│
├── README.md
├── LICENSE
└── .gitignore
```

## Architecture

The application is separated into modules, with each module handling a specific responsibility.

### `main.py`

Controls the application flow.

Responsibilities:

- Display the menu
- Receive user commands
- Execute the selected operation

### `expenses.py`

Contains the core expense management functionality.

Responsibilities:

- Add expenses
- View expenses
- Search expenses
- Edit expenses
- Delete expenses

### `inputs.py`

Handles user input and validation.

Responsibilities:

- Validate dates
- Validate expense amounts
- Validate categories
- Validate descriptions

### `storage.py`

Handles data persistence.

Responsibilities:

- Load expenses from CSV
- Save expenses to CSV
- Validate CSV structure

### `reports.py`

Contains reporting functions.

Current functionality:

- Calculate total spending

## Technologies Used

- Python 3
- CSV file handling
- `pathlib`
- Type hints
- Modular programming
- Command-line interface (CLI)

## Installation

Clone the repository:

```bash
git clone https://github.com/elinavt/budget-tracker-.git
```

Navigate into the project folder:

```bash
cd budget-tracker-
```

## Running the Application

Run the application from the project root:

```bash
python -m src.main
```

## Example Usage

```text
==== Budget Tracker ====

1. Add expense
2. View expenses
3. Show total spending
4. Search by category
5. Delete expense
6. Edit expense
7. Exit
```

Example expense output:

```text
Date: 2026-08-03
Category: Food
Amount: 15.50
Description: Lunch
------------------------------
```

## Data Storage

Expenses are stored in:

```text
data/expenses.csv
```

The CSV format is:

```csv
date,amount,category,description
```

Example:

```csv
2026-08-03,15.50,Food,Lunch
```

The repository contains only an empty CSV file with headers to demonstrate the required format. No personal financial data is included.

## Skills Demonstrated

### Python Programming

- Functions
- Modules
- File handling
- Error handling
- Data structures
- Type hints
- Documentation

### Software Engineering

- Separation of concerns
- Modular architecture
- Reusable components
- Defensive programming
- Persistent storage

## Design Decisions

### CSV Storage

CSV was selected as a lightweight storage solution because it is simple, human-readable, and suitable for a small command-line application.

### Modular Structure

The project separates user interaction, validation, storage, and business logic. This makes the code easier to maintain and extend.

### Input Validation

User input is validated before being stored to reduce errors and maintain consistent data.

## Future Improvements

Possible future extensions:

- Pandas-based expense analysis
- Data visualization with Matplotlib
- Monthly spending reports
- Budget limits and alerts
- SQLite database storage
- Graphical user interface

## License

This project is licensed under the MIT License.
