import unittest
from sudoku_solver.model import SudokuModel

class TestSudokuModel(unittest.TestCase):

    def setUp(self):
        self.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.model = SudokuModel(self.grid)

    def test_is_valid(self):
        self.assertTrue(self.model.is_valid(0, 2, 4))  # Valid move
        self.assertFalse(self.model.is_valid(0, 2, 3))  # Invalid move

    def test_solve_backtracking(self):
        self.assertTrue(self.model.solve_backtracking())  # Should solve successfully
