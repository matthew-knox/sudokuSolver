

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku Solver")

    view = SudokuView(root)
    controller = SudokuController(view)

    # Add the solve and clear button functions
    solve_button = tk.Button(root, text="Solve", command=controller.start_solver,
                             bg='green', fg='white', font=("Arial", 16, "bold"), width=10, height=2)
    solve_button.grid(row=2, column=0, pady=10)

    clear_button = tk.Button(root, text="Clear Puzzle", command=controller.clear_puzzle,
                             bg='red', fg='white', font=("Arial", 12), width=10, height=1)
    clear_button.grid(row=3, column=0, pady=10)

    root.mainloop()
