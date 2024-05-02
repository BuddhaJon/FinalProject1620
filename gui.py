import tkinter as tk
from interest_calculator_gui import InterestCalculatorApp
from net_worth_gui import NetWorthApp
from budget_gui import BudgetApp
from inflation_calculator_gui import InflationCalculatorApp
from loan_calculator_gui import LoanCalculatorApp


class MainApp:
    """Main application GUI class for navigating between financial tools."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the main application GUI and set up navigation buttons."""
        self.root = root
        root.title('Personal Finance App')  # Set the window title here
        root.geometry('400x300')  # Adjust the size of the main window
        root.configure(bg='blue')  # Set a background color

        # Create a title label
        title_label = tk.Label(root, text="Personal Finance", font=("Arial", 16, "bold"), bg='blue')
        title_label.pack(pady=10)

        # Setup buttons for navigation
        tk.Button(root, text='Budgeting Tool', command=self.open_budget_tool).pack(pady=10)
        tk.Button(root, text='Interest Calculator', command=self.open_interest_calculator).pack(pady=10)
        tk.Button(root, text='Net Worth Calculator', command=self.open_net_worth_calculator).pack(pady=10)
        tk.Button(root, text='Inflation Calculator', command=self.open_inflation_calculator).pack(pady=10)
        tk.Button(root, text='Loan Interest Calculator', command=self.open_loan_calculator).pack(pady=10)


    def open_interest_calculator(self) -> None:
        """Open the interest calculator tool."""
        top = tk.Toplevel(self.root)
        InterestCalculatorApp(top)

    def open_net_worth_calculator(self) -> None:
        """Open the net worth calculator tool."""
        top = tk.Toplevel(self.root)
        NetWorthApp(top)

    def open_budget_tool(self) -> None:
        """Open the budgeting tool."""
        top = tk.Toplevel(self.root)
        BudgetApp(top)

    def open_inflation_calculator(self) -> None:
        """Open the inflation calculator tool."""
        top = tk.Toplevel(self.root)
        InflationCalculatorApp(top)

    def open_loan_calculator(self) -> None:
        """Open the inflation calculator tool."""
        top = tk.Toplevel(self.root)
        LoanCalculatorApp(top)
