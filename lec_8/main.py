import random

class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def mean(self):
        flat_matrix = [num for row in self.matrix for num in row]
        return sum(flat_matrix) / (self.rows * self.cols)

    def row_sum(self, row_index):
        if 0 <= row_index < self.rows:
            return sum(self.matrix[row_index])
        return None

    def col_average(self, col_index):
        if 0 <= col_index < self.cols:
            col = [row[col_index] for row in self.matrix]
            return sum(col) / self.rows
        return None

    def print_submatrix(self, submatrix):
        col1, col2, row1, row2 = submatrix
        if 0 <= row1 < row2 <= self.rows and 0 <= col1 < col2 <= self.cols:
            submatrix_data = [row[col1:col2] for row in self.matrix[row1:row2]]
            submatrix_str = '\n'.join(['\t'.join(map(str, row)) for row in submatrix_data])
            print(submatrix_str)

n = 4
m = 3
matrix = Matrix(n, m)
print("Matrix:")
print(matrix)

matrix_mean = matrix.mean()
print(f"Mean of the matrix: {matrix_mean:.2f}")

row_index = 2
row_sum = matrix.row_sum(row_index)
print(f"Sum of row {row_index}: {row_sum}")

col_index = 1
col_average = matrix.col_average(col_index)
print(f"Average of column {col_index}: {col_average:.2f}")

submatrix_coordinates = [1, 3, 0, 2]
print("Submatrix:")
matrix.print_submatrix(submatrix_coordinates)
