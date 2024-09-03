import json
import sys

def add_expense(expenses, amount, description):
    expenses.append({'amount': amount, 'description': description})

def save_expenses(expenses, filename):
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent=4)

def load_expenses(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [add|list] [amount] [description]")
        return
    command = sys.argv[1]
    filename = 'expenses.json'
    expenses = load_expenses(filename)
    
    if command == 'add':
        if len(sys.argv) != 4:
            print("Usage: python script.py add [amount] [description]")
            return
        amount = float(sys.argv[2])
        description = sys.argv[3]
        add_expense(expenses, amount, description)
        save_expenses(expenses, filename)
        print("Expense added.")
    
    elif command == 'list':
        total = sum(expense['amount'] for expense in expenses)
        print("Expenses:")
        for expense in expenses:
            print(f"{expense['description']}: ${expense['amount']:.2f}")
        print(f"Total: ${total:.2f}")
    
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
