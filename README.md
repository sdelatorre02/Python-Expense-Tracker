# Expense Tracker

## Description
The Expense Tracker is a command-line Python application designed to help users manage their personal finances. Users can add expenses, view a list of their recorded expenses, generate summary reports by category, and save or load their expense data to/from a file.

## Features
- **Add Expense**: Input details of an expense including amount, category, and description.
- **View Expenses**: Display all recorded expenses with details.
- **Generate Report**: Summarize total expenses by category.
- **Save Expenses**: Save the list of expenses to a JSON file.
- **Load Expenses**: Load the list of expenses from a JSON file.

## Installation
1. Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository or download the source code.

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

## Usage
1. Navigate to the project directory.
2. Run the expense_tracker.py script.
3. Follow the on-screen instructions to interact with the application.

## Project Structure
- **'expense_tracker.py'**: Main script that contains the Expense Tracker application logic.
- **'expenses.json'** (optional): Example JSON file to demonstrate loading and saving functionality.

## Error Handling
- Ensures amount is a valid numerical value
- Ensures category and description are string values
- Handles file-related errors (e.g., file not found, JSON decode errors).

## Contact
For any inquires, please contact '**sdelatorre2@yahoo.com**
