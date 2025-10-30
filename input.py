#  User Input

# Ask the user for two numbers
print("=== Simple Arithmetic Calculator ===")

# Taking input (input() always returns a string, so we convert it to float)
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_ = a + b
difference = a - b
product = a * b
quotient = a / b
floor_div = a // b
remainder = a % b
power = a ** b

# Print the results in a nice format
print("\n=== Results ===")
print("You entered:", a, "and", b)
print("Sum:", sum_)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Floor Division:", floor_div)
print("Remainder:", remainder)
print("Power (a ** b):", power)

