import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def toDict(self):
        return{
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }
    
class ExpenseTracker:
    def __init__(self):
        self.expense = []
    
    def addExpense(self, amount, category, description):
        if not isinstance(amount, (int, float)):
            print("Error: Amount must be a numerical value.")
            return
        if not isinstance(category,str) or not isinstance(description, str):
            print("Error: Category and description must be a string.")
            return
        expense = Expense(amount, category, description)
        self.expense.append(expense)
        print(f"Expense: {amount} in {category} for '{description}' added")
    
    def viewExpense(self):
        if not self.expense:
            print("No expenses.")
            return
        for expense in self.expense:
            print(f"{expense.date} - {expense.category}: ${expense.amount} - {expense.description}")
    
    def expenseReport(self):
        if not self.expense:
            print("No expenses to report.")
            return
        report = {}
        for expenses in self.expense:
            if expenses.category in report:
                report[expenses.category] += expenses.amount
            else:
                report[expenses.category] = expenses.amount
        print("Expense Report:")
        for category, total in report.items():
            print(f"{category}: ${total}")
    
    def saveExpense(self,filename):
        try:
            with open(filename, 'w') as f:
                json.dump([expense.toDict() for expense in self.expense], f)
            print(f"Expenses saved to {filename}")
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def loadExpense(self, filename):
        try:
            with open(filename, 'r') as f:
                expense = json.load(f)
                self.expense = [Expense(**expense) for expense in expense]
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"No file found with the name {filename}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}")
        except TypeError as e:
            print(f"Error loading expenses: {e}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Generate Report\n4. Save Expenses\n5. Load Expenses\n6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                tracker.addExpense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")
        elif choice == '2':
            tracker.viewExpense()
        elif choice == '3':
            tracker.expenseReport()
        elif choice == '4':
            filename = input("Enter filename to save: ")
            tracker.saveExpense(filename)
        elif choice == '5':
            filename = input("Enter filename to load: ")
            tracker.loadExpense(filename)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
