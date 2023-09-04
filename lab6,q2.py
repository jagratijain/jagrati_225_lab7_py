import numpy as np

# Create two NumPy arrays as sets
set1 = np.array([1, 2, 3, 4, 5])
set2 = np.array([3, 4, 5, 6, 7])

# Union (Unique elements from both sets)
union_result = np.union1d(set1, set2)

# Intersection (Common elements in both sets)
intersection_result = np.intersect1d(set1, set2)

# Set difference (Elements in set1 but not in set2)
difference_result = np.setdiff1d(set1, set2)

# XOR (Symmetric Difference - Elements that are in either of the sets, but not in both)
xor_result = np.setxor1d(set1, set2)

# Print the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union Result:", union_result)
print("Intersection Result:", intersection_result)
print("Set Difference Result:", difference_result)
print("XOR Result:", xor_result)
