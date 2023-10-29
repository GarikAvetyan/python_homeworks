import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    column_sum = 0
    for row in matrix:
        if 0 <= column_index < len(row):
            column_sum += row[column_index]
    return column_sum

def get_row_average(matrix, row_index):
    if 0 <= row_index < len(matrix):
        row = matrix[row_index]
        if len(row) > 0:
            return sum(row) / len(row)
    return 0

rows = 3
cols = 4
matrix = generate_random_matrix(rows, cols)
print("Random Matrix:")
for row in matrix:
    print(row)

column_index = 2
column_sum = get_column_sum(matrix, column_index)
print(f"Sum of column {column_index}: {column_sum}")

row_index = 1
row_average = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {row_average}")