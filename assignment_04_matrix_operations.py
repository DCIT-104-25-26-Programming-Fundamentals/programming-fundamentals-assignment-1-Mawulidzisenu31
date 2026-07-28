# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# Matrix Operations
# =============================================================================

def read_matrix(rows, cols, name="matrix"):
    print(f"Enter {name} ({rows} rows, {cols} values per row, space-separated):")
    matrix = []
    for i in range(rows):
        while True:
            entries = input(f"Enter row {i + 1}: ").split()
            if len(entries) != cols:
                print(f"  Expected {cols} numbers, got {len(entries)}. Try again.")
                continue
            row = [float(x) for x in entries]
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix):
    widths = []
    for j in range(len(matrix[0])):
        col_width = max(len(format_num(matrix[i][j])) for i in range(len(matrix)))
        widths.append(col_width)

    for row in matrix:
        formatted = [format_num(val).rjust(widths[j]) for j, val in enumerate(row)]
        print("  ".join(formatted))


def format_num(x):
    if x == int(x):
        return str(int(x))
    return f"{x:g}"


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols, "the matrix")

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transpose(matrix))


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = read_matrix(rows, cols, "matrix A")
    matrix_b = read_matrix(rows, cols, "matrix B")

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    print("\nSum (A + B):")
    print_matrix(add_matrices(matrix_a, matrix_b))


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of matrix A: "))
    n = int(input("Enter columns of matrix A (= rows of matrix B): "))
    p = int(input("Enter columns of matrix B: "))

    matrix_a = read_matrix(m, n, "matrix A")
    matrix_b = read_matrix(n, p, "matrix B")

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    print("\nProduct (A x B):")
    print_matrix(multiply_matrices(matrix_a, matrix_b))


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix (Part A)")
    print("2. Add Two Matrices (Part B)")
    print("3. Multiply Two Matrices (Part C)")

    choice = input("Choose an operation (1/2/3): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
