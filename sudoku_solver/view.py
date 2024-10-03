import tkinter as tk

class SudokuView:
    """View for displaying the Sudoku puzzle in the GUI."""

    def __init__(self, root):
        self.root = root
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.timer_label = None
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        """Create the Sudoku grid in the GUI."""
        grid_frame = tk.Frame(self.root)
        grid_frame.grid(row=0, column=0, padx=10, pady=10)

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(grid_frame, width=3, justify='center', font=("Arial", 18))
                padx = (2, 2)
                pady = (2, 2)
                if col in [3, 6]:
                    padx = (10, 2)
                if row in [3, 6]:
                    pady = (10, 2)
                entry.grid(row=row, column=col, padx=padx, pady=pady, ipady=10)
                self.entries[row][col] = entry

    def create_buttons(self):
        """Create buttons and timer label for the GUI."""
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=20)

        # Timer Label
        self.timer_label = tk.Label(button_frame, text="Time: 0.00s", font=("Arial", 12))
        self.timer_label.grid(row=1, column=0, columnspan=4, pady=10)

    def clear_grid(self):
        """Clear all the entries in the grid."""
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)

    def update_grid(self, grid):
        """Update the GUI grid with the solved numbers."""
        for row in range(9):
            for col in range(9):
                if grid[row][col] != 0:
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].insert(0, str(grid[row][col]))
