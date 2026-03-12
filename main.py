class Expenses:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount
          
    def __str__(self):
        return f"{self.name} | {self.category} | {self.amount}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        
    def show_expense(self):
        if not self.expenses:
            print("No expenses added.")
        else:
            for index, value in enumerate(self.expenses, start=1):
                print(f"{index}. {value}")
         
    def add_expense(self, add_name, add_category, add_amount):
        user_expense = Expenses(add_name, add_category, add_amount)
        self.expenses.append(user_expense)
        print("Expense added successfully.")
        
    def update_expense(self, index, field, new_value):
        if not self.expenses:
            print("No expenses to update.")
        elif index < 0 or index >= len(self.expenses):
            print("Invalid index.")
        else:
            expense = self.expenses[index]
            
            if field == 'name':
                expense.name = new_value
            elif field == 'category':
                expense.category = new_value
            elif field == 'amount':
                expense.amount = new_value
                
            print("Expense updated successfully.")
    
    
    def total_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            total = 0
            for expense in self.expenses:
                total += expense.amount
            print(f"Total expense: {total}")

    
    def delete_expense(self, user_delete):
        if not self.expenses:
            print("No expenses to delete.")
        elif user_delete < 0 or user_delete >= len(self.expenses):
            print("Invalid index.")
        else:
            deleted = self.expenses.pop(user_delete)
            print(f"Expense deleted: {deleted}")

expense_tracker = ExpenseTracker()


while True:
    print("\n1. SHOW \n2. ADD\n3. UPDATE \n4. SUM \n5. DELETE \n6. EXIT")
    choice = input("Choose a number to perform the operation: ").strip()
    
    if choice == '1':
        expense_tracker.show_expense()
        
    elif choice == '2':
        add_name = input("Enter name: ")
        add_category = input("Enter category: ")
        add_amount = int(input("Enter amount: "))
        expense_tracker.add_expense(add_name, add_category, add_amount)
    
    elif choice == '3':
        expense_tracker.show_expense()
        index = int(input("Enter index to update: ")) - 1
        
        print("1. Update name")
        print("2. Update category")
        print("3. Update amount")
        
        user_input = input("Enter choice: ")
        
        if user_input == '1':
            new_value = input("Enter new name: ")
            expense_tracker.update_expense(index, "name", new_value)
            
        elif user_input == '2':
            new_value = input("Enter new category: ")
            expense_tracker.update_expense(index, "category", new_value)
            
        elif user_input == '3':
            new_value = int(input("Enter new amount: "))
            expense_tracker.update_expense(index, "amount", new_value)
    
    elif choice == '4':
        expense_tracker.total_expense()
    
    elif choice == '5':
        expense_tracker.show_expense()
        user_delete = int(input("Enter index to delete: ")) - 1
        expense_tracker.delete_expense(user_delete)
        
    elif choice == '6':
        print("Exiting program.")
        break