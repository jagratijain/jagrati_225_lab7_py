import numpy as np

# Create two random 3x3 matrices
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

# Product (element-wise product)
product_result = np.multiply(matrix1, matrix2)

# Multiplication (matrix multiplication)
multiplication_result = np.matmul(matrix1, matrix2)

# Dot Product (dot product of flattened arrays)
dot_product_result = np.dot(matrix1.flatten(), matrix2.flatten())

# Print the results
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nProduct Result:")
print(product_result)
print("\nMultiplication Result:")
print(multiplication_result)
print("\nDot Product Result:")
print(dot_product_result)
