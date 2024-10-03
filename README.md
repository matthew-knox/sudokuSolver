# Sudoku Solver Project

This is a Python-based Sudoku solver application built with a Model-View-Controller (MVC) architecture. It includes a graphical user interface (GUI) for entering Sudoku puzzles and solving them using a backtracking algorithm.

## Features

- **Solve Sudoku puzzles** with an option to visualize the solving process.
- **Clear the puzzle** to reset the grid.
- **Paste puzzles** directly into the grid from the clipboard.
- **Real-time timer** to track how long the solver takes to solve the puzzle.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/sudoku_solver_project.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application by executing the `main.py` file:
```bash
python main.py
```

You can enter your Sudoku puzzle manually, or paste it directly from the clipboard. Once entered, click "Solve" to solve the puzzle, and "Clear" to reset the grid.

## Running Tests

To run the unit tests:
```bash
pytest
```

## License

This project is licensed under the MIT License.