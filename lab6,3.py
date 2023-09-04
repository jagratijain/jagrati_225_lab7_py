import numpy as np

# Create a random 1D array
array = np.random.rand(10)  # Adjust the size as needed

# Cumulative sum
cumulative_sum = np.cumsum(array)

# Cumulative Product
cumulative_product = np.cumprod(array)

# Discrete difference with n=3
discrete_difference = np.diff(array, n=3)

# Find unique elements in the array
unique_elements = np.unique(array)

# Print the results
print("Original Array:")
print(array)
print("\nCumulative Sum:")
print(cumulative_sum)
print("\nCumulative Product:")
print(cumulative_product)
print("\nDiscrete Difference (n=3):")
print(discrete_difference)
print("\nUnique Elements:")
print(unique_elements)
