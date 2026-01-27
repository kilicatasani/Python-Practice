def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# Example
print(f"GCD of 48 and 18 is: {gcd_recursive(48, 18)}") # Result: 6
