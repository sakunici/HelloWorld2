import json
import os

class KidFinancialManagementGame:
    def __init__(self, file_path='kids_finance.json'):
        self.file_path = file_path
        self.data = self.load_data()
        
    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def create_kid(self, name):
        if name in self.data:
            print(f"Kid {name} already exists.")
        else:
            self.data[name] = {
                'allowance': 0,
                'expenses': [],
                'savings_goal': 0,
                'current_savings': 0
            }
            self.save_data()
            print(f"Kid {name} added.")

    def set_allowance(self, name, amount):
        if name in self.data:
            self.data[name]['allowance'] = amount
            self.save_data()
            print(f"Allowance for {name} set to {amount}.")
        else:
            print(f"Kid {name} does not exist.")

    def add_expense(self, name, expense, amount):
        if name in self.data:
            self.data[name]['expenses'].append({'expense': expense, 'amount': amount})
            self.save_data()
            print(f"Expense {expense} of {amount} added for {name}.")
        else:
            print(f"Kid {name} does not exist.")

    def set_savings_goal(self, name, goal):
        if name in self.data:
            self.data[name]['savings_goal'] = goal
            self.save_data()
            print(f"Savings goal for {name} set to {goal}.")
        else:
            print(f"Kid {name} does not exist.")

    def add_savings(self, name, amount):
        if name in self.data:
            self.data[name]['current_savings'] += amount
            self.save_data()
            print(f"Added {amount} to {name}'s savings.")
        else:
            print(f"Kid {name} does not exist.")

    def show_summary(self, name):
        if name in self.data:
            kid = self.data[name]
            print(f"Summary for {name}:")
            print(f"  Allowance: {kid['allowance']}")
            print(f"  Current Savings: {kid['current_savings']}")
            print(f"  Savings Goal: {kid['savings_goal']}")
            print("  Expenses:")
            for expense in kid['expenses']:
                print(f"    {expense['expense']}: {expense['amount']}")
        else:
            print(f"Kid {name} does not exist.")

def main():
    game = KidFinancialManagementGame()

    while True:
        print("\nKid's Financial Management Game")
        print("1. Add Kid")
        print("2. Set Allowance")
        print("3. Add Expense")
        print("4. Set Savings Goal")
        print("5. Add Savings")
        print("6. Show Summary")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter kid's name: ")
            game.create_kid(name)
        elif choice == '2':
            name = input("Enter kid's name: ")
            amount = float(input("Enter allowance amount: "))
            game.set_allowance(name, amount)
        elif choice == '3':
            name = input("Enter kid's name: ")
            expense = input("Enter expense: ")
            amount = float(input("Enter amount: "))
            game.add_expense(name, expense, amount)
        elif choice == '4':
            name = input("Enter kid's name: ")
            goal = float(input("Enter savings goal: "))
            game.set_savings_goal(name, goal)
        elif choice == '5':
            name = input("Enter kid's name: ")
            amount = float(input("Enter amount to add to savings: "))
            game.add_savings(name, amount)
        elif choice == '6':
            name = input("Enter kid's name: ")
            game.show_summary(name)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
