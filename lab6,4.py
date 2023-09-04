import numpy as np

# Create two 1D arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Addition using zip()
result_zip = np.array([a + b for a, b in zip(array1, array2)])

# Addition using np.add()
result_np_add = np.add(array1, array2)

# User-defined addition function
def user_defined_add(x, y):
    return x + y

# Create a ufunc from the user-defined function
ufunc = np.frompyfunc(user_defined_add, 2, 1)

# Addition using the user-defined function
result_user_defined = ufunc(array1, array2)

# Print the results
print("Array 1:", array1)
print("Array 2:", array2)
print("\nAddition using zip():", result_zip)
print("Addition using np.add():", result_np_add)
print("Addition using user-defined function:", result_user_defined)
