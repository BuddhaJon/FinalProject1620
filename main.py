import tkinter as tk
from gui import MainApp

def main() -> None:
    """Initialize the main application window."""
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
