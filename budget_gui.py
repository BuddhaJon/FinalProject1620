import tkinter as tk

class BudgetApp:
    """GUI class for the Budgeting Tool with dynamic expense entries including labels."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the budgeting tool GUI with dynamic expense entry fields."""
        self.root = root
        root.title('Budgeting Tool')
        root.geometry('400x600')  # Set the window size

        tk.Label(root, text='Monthly Income ($):').pack()
        self.income_entry = tk.Entry(root)
        self.income_entry.pack()

        self.expenses_frame = tk.Frame(root)
        self.expenses_frame.pack()

        tk.Button(root, text='Add Expense', command=self.add_expense_field).pack()

        self.calculate_button = tk.Button(root, text='Calculate Balance', command=self.calculate_balance)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text='Balance: $0.00')
        self.result_label.pack()

        self.expenses = []

    def add_expense_field(self) -> None:
        """Add entry fields for labeled expenses."""
        frame = tk.Frame(self.expenses_frame)
        frame.pack()

        tk.Label(frame, text='Expense Name:').pack(side=tk.LEFT)
        label_entry = tk.Entry(frame, width=15)
        label_entry.pack(side=tk.LEFT)

        tk.Label(frame, text='Amount ($):').pack(side=tk.LEFT)
        amount_entry = tk.Entry(frame, width=15)
        amount_entry.pack(side=tk.LEFT)

        self.expenses.append((label_entry, amount_entry))

    def calculate_balance(self) -> None:
        """Calculate and display the monthly balance after summing labeled expenses."""
        try:
            income = float(self.income_entry.get().replace('$', '').replace(',', '').strip())
            total_expenses = sum(float(expense[1].get().replace('$', '').replace(',', '').strip()) for expense in self.expenses if expense[1].get())

            balance = income - total_expenses
            self.result_label.config(text=f'Balance: ${balance:,.2f}')
        except ValueError:
            self.result_label.config(text=f'Please enter only numbers.')
