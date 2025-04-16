matrix_a = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 5, 4, 1, 3],
    [4, 1, 5, 3, 2],
    [3, 5, 1, 2, 4],
]

matrix_b = [
    [6, 7, 8, 9, 3],
    [7, 9, 4, 6, 8],
    [9, 8, 2, 6, 7],
    [8, 7, 9, 5, 6],
    [3, 9, 7, 8, 6],
]

hasil = []

# Perkalian matriks
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_b[0])):
        cell = 0
        for k in range(len(matrix_b)):
            cell += matrix_a[i][k] * matrix_b[k][j]
        row.append(cell)
    hasil.append(row)

for row in hasil:
    print(row)
