class SudokuModel:
    """Model for solving the Sudoku puzzle."""

    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        """Check if placing num in grid[row][col] is valid."""
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_backtracking(self):
        """Backtracking algorithm to solve the puzzle."""
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve_backtracking():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True
