import tkinter as tk
from inflation_calculator import InflationCalculator

class InflationCalculatorApp:
    """GUI class for the compound interest calculator."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the interest calculator GUI."""
        self.root = root
        root.title('Inflation Calculator')
        root.geometry('400x300')  # Set the window size

        # Create and place GUI components
        tk.Label(root, text='Principal ($):').pack()
        self.principal_entry = tk.Entry(root)
        self.principal_entry.pack()

        tk.Label(root, text='Years:').pack()
        self.years_entry = tk.Entry(root)
        self.years_entry.pack()

        tk.Button(root, text='Calculate', command=self.perform_calculation).pack()

        self.result_label = tk.Label(root, text='Result:')
        self.result_label.pack()

    def perform_calculation(self) -> None:
        """Calculate and display the compound interest based on user input."""
        try:
            principal = float(self.principal_entry.get().replace(',', '').strip())
            rate = -0.035
            years = int(self.years_entry.get().strip())
            calculator = InflationCalculator()
            result = calculator.calculate(principal, rate, years)
            self.result_label.config(text=f'Result: ${result:,.2f}')
        except ValueError as e:
            self.result_label.config(text=f'Error: {str(e)}')
