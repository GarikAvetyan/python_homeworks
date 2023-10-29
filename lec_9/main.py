class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is not None:
            if len(data) != rows:
                raise ValueError("Number of rows in data must match the specified rows.")
            for row in data:
                if len(row) != columns:
                    raise ValueError("Number of columns in data must match the specified columns.")
            self.data = data
        else:
            self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for addition.")
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result_data)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for subtraction.")
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result_data)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        result_data = [[0 for _ in range(other.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result_data[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(self.rows, other.columns, result_data)

matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix 1 + Matrix 2:")
print(matrix1 + matrix2)

print("\nMatrix 1 - Matrix 2:")
print(matrix1 - matrix2)

matrix3 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
matrix4 = Matrix(2, 4, [[7, 8, 9, 10], [11, 12, 13, 14]])

print("\nMatrix 3:")
print(matrix3)

print("\nMatrix 4:")
print(matrix4)

print("\nMatrix 3 * Matrix 4:")
print(matrix3 * matrix4)