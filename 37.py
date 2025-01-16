# Perform matrix addition
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1 = [[int(input(f"Enter element for Matrix1[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
matrix2 = [[int(input(f"Enter element for Matrix2[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
print("Resultant Matrix:")
for row in result:
    print(row)
    