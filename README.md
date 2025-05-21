Sparse Matrix Implementation...

This project implements a sparse matrix data structure in Python for the "Data Structures and Algorithms for Engineers" Programming Assignment 2. It uses a Coordinate List (COO) format for memory efficiency and supports addition, subtraction, and multiplication. Some matrix inputs may cause errors (e.g., dimension mismatches).

  

Prerequisites...

Git
Python 3.6+
VS Code

Setup...

Clone Repository


Verify Files:

Ensure dsa/sparse_matrix/code/sparse_matrix.py exists.
Check sample_inputs/ for input files.
Create outputs/:mkdir -p dsa/sparse_matrix/outputs




Set Python:

Install Python 3.6+.
In VS Code: Ctrl+Shift+P > Python: Select Interpreter.



Running

Open sparse_matrix.py in VS Code.
Run:cd dsa/sparse_matrix/code/src
python3 sparse_matrix.py


Choose operation (1: Add, 2: Subtract, 3: Multiply, 4: Exit) and enter file paths (e.g., ../../sample_inputs/matrix1.txt).

Notes

Errors: May occur for mismatched dimensions (e.g., addition requires same rows/cols) or invalid file formats. Use compatible matrices.
Format: Input/output files use rows=<num>, cols=<num>, (row, col, value).
No external libraries used.

