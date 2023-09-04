from functools import reduce
import math

# Define a function to calculate the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Define a function to calculate the LCM of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Create an array of elements
elements = [12, 18, 24, 36, 48]

# Find the GCD of the elements using reduce()
gcd_result = reduce(gcd, elements)

# Find the LCM of the elements using reduce()
lcm_result = reduce(lcm, elements)

# Print the results
print("Array of Elements:", elements)
print("GCD of Elements:", gcd_result)
print("LCM of Elements:", lcm_result)
