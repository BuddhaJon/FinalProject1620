import tkinter as tk

class NetWorthApp:
    """GUI class for the Net Worth Calculator with detailed asset categories."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the net worth calculator GUI with specific asset fields."""
        self.root = root
        root.title('Net Worth Calculator')
        root.geometry('400x400')  # Set the window size

        self.assets = {}

        # Asset entries
        self.create_asset_entry('House ($):', 'house')
        self.create_asset_entry('Car ($):', 'car')
        self.create_asset_entry('Savings ($):', 'savings')
        self.create_asset_entry('Investing Account ($):', 'investing')
        self.create_asset_entry('Retirement Funds ($):', 'retirement')
        self.create_asset_entry('Valuables ($):', 'valuables')

        tk.Label(root, text='Total Liabilities ($):').pack()
        self.liabilities_entry = tk.Entry(root)
        self.liabilities_entry.pack()

        tk.Button(root, text='Calculate Net Worth', command=self.calculate_net_worth).pack()

        self.result_label = tk.Label(root, text='Net Worth: $0.00')
        self.result_label.pack()

    def create_asset_entry(self, label_text: str, asset_name: str) -> None:
        """Helper function to create labeled entry for each asset."""
        tk.Label(self.root, text=label_text).pack()
        entry = tk.Entry(self.root)
        entry.pack()
        self.assets[asset_name] = entry

    def calculate_net_worth(self) -> None:
        """Calculate and display net worth based on assets and liabilities."""
        try:
            total_assets = sum(float(self.assets[asset].get().replace(',', '').strip()) for asset in self.assets)
            liabilities = float(self.liabilities_entry.get().replace(',', '').strip())
            net_worth = total_assets - liabilities
            self.result_label.config(text=f'Net Worth: ${net_worth:,.2f}')
        except ValueError as e:
            self.result_label.config(text=f'Error: {str(e)}')
