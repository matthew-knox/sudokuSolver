from setuptools import setup, find_packages

setup(
    name='sudoku_solver_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tkinter',  # You might not need to specify tkinter since it's part of the standard library
    ],
    entry_points={
        'console_scripts': [
            'sudoku_solver = sudoku_solver.main:main',
        ]
    }
)
