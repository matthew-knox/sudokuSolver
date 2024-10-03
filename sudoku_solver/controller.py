import time


class SudokuController:
    """Controller to manage interactions between the view and model."""

    def __init__(self, view):
        self.view = view
        self.model = None
        self.start_time = 0

    def get_grid_from_view(self):
        """Retrieve the grid from the view (UI) and convert to a 2D list."""
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.view.entries[row][col].get()
                if value.isdigit():
                    current_row.append(int(value))
                else:
                    current_row.append(0)
            grid.append(current_row)
        return grid

    def start_solver(self):
        """Start solving the puzzle and update the UI."""
        grid = self.get_grid_from_view()
        self.model = SudokuModel(grid)
        self.start_time = time.time()

        if self.model.solve_backtracking():
            self.view.update_grid(self.model.grid)
            elapsed_time = time.time() - self.start_time
            self.view.timer_label.config(text=f"Time: {elapsed_time:.2f}s")
        else:
            self.view.timer_label.config(text="No solution found.")

    def clear_puzzle(self):
        """Clear the puzzle and reset the timer."""
        self.view.clear_grid()
        self.view.timer_label.config(text="Time: 0.00s")
