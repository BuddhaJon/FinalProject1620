import tkinter as tk
from loan_calculator import LoanCalculator, LoanCalculatorSimple

class LoanCalculatorApp:
    """GUI class for the compound interest calculator."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the interest calculator GUI."""
        self.root = root
        root.title('Loan Interest Calculator')
        root.geometry('400x300')  # Set the window size

        # Create and place GUI components
        tk.Label(root, text='Principal ($):').pack()
        self.principal_entry = tk.Entry(root)
        self.principal_entry.pack()

        tk.Label(root, text='Interest Rate (%):').pack()
        self.rate_entry = tk.Entry(root)
        self.rate_entry.pack()

        tk.Label(root, text='Years:').pack()
        self.years_entry = tk.Entry(root)
        self.years_entry.pack()

        tk.Button(root, text='Calculate Compound Interest:', command=self.perform_compound_calculation).pack()
        tk.Button(root, text='Calculate Simple Interest:', command=self.perform_calculation).pack()


        self.result_label = tk.Label(root, text='Result:')
        self.result_label.pack()

    def perform_compound_calculation(self) -> None:
        """Calculate and display the compound interest based on user input."""
        try:
            principal = float(self.principal_entry.get().replace(',', '').strip())
            rate = float(self.rate_entry.get().strip()) / 100  # Convert percentage to decimal
            years = int(self.years_entry.get().strip())
            calculator = LoanCalculator()
            result = calculator.CompoundCalculator(principal, rate, years)
            self.result_label.config(text=f'Interest Paid: ${result:,.2f}')
        except ValueError as e:
            self.result_label.config(text=f'Error: {str(e)}')

    def perform_calculation(self) -> None:
        """Calculate and display the compound interest based on user input."""
        try:
            principal = float(self.principal_entry.get().replace(',', '').strip())
            rate = float(self.rate_entry.get().strip()) / 100  # Convert percentage to decimal
            years = int(self.years_entry.get().strip())
            calculator = LoanCalculatorSimple()
            result = calculator.Calculate(principal, rate, years)
            self.result_label.config(text=f'Interest Paid: ${result:,.2f}')
        except ValueError as e:
            self.result_label.config(text=f'Error: {str(e)}')