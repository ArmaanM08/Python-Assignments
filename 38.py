# Transpose a matrix
matrix = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(3)] for i in range(3)]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transpose:")
for row in transpose:
    print(row)